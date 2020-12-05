#!/bin/bash

# エラー終了
exit_error() {
  if [ -n "$1" ]; then
    echo_error $1
  fi
  exit 1
}

# ==================================================
# echo with color
# ==================================================
ECHO_ESC=$(printf '\033')

ECHO_COLORS_RED=1
ECHO_COLORS_GREEN=2
ECHO_COLORS_YELLOW=3
ECHO_COLORS_BLUE=4
ECHO_COLORS_PURPLE=5
ECHO_COLORS_AQUA=6

ECHO_TYPE_TEXT=3
ECHO_TYPE_BACKGROUND=4

echo_color() {
  ECHO_COLOR=$1
  shift
  echo "${ECHO_ESC}[${ECHO_TYPE_TEXT}${ECHO_COLOR}m$@${ECHO_ESC}[m"
}

echo_info() {
  echo_color $ECHO_COLORS_AQUA "$@"
}

echo_warn() {
  echo_color $ECHO_COLORS_YELLOW "$@"
}

echo_error() {
  echo_color $ECHO_COLORS_RED "$@"
}

# 呼び出し元のメソッド名をecho
echo_exec_method() {
  echo_info "called: ${FUNCNAME[1]}"
}

# ==================================================
# run with echo
# ==================================================
run_with_echo() {
  echo_info "$@"
  "$@"
}

# ==================================================
# OSの判定処理
# ==================================================
OS_MAC="Mac"
OS_LINUX="Linux"
OS_CYGWIN="Cygwin"

analyze_os() {
  OS=""
  if [ "$(uname)" == 'Darwin' ]; then
    OS=$OS_MAC
    IS_MAC=1
  elif [ "$(expr substr $(uname -s) 1 5)" == 'Linux' ]; then
    OS=$OS_LINUX
    IS_LINUX=1
  elif [ "$(expr substr $(uname -s) 1 10)" == 'MINGW32_NT' ]; then                                                                                           
    OS=$OS_CYGWIN
    IS_WIN=1
  elif [ "$(expr substr $(uname -s) 1 10)" == 'MINGW64_NT' ]; then                                                                                           
    OS=$OS_CYGWIN
    IS_WIN=1
  fi
}

# ==================================================
# パラメータチェック
# ==================================================
# 値が存在しなければエラー
if_not_exit() {
  if [ -z "$1" ]; then
    exit_error "$2"
  fi
}

# ==================================================
# 特定の環境変数が設定されているかをチェックする
# ==================================================
# ENVS=(a b c)
# envs_check ${ENVS[*]}
envs_check() {
  for env in "$@"; do
    if [ -z "${!env}" ]; then
      echo_error $env is not set
      exit 1
    fi
  done
}

# ==================================================
# git
# ==================================================
git_update() {
  run_with_echo git pull
  run_with_echo git checkout .
  run_with_echo git submodule update --init --recursive
  run_with_echo git submodule foreach git pull
  run_with_echo git submodule foreach git checkout .
}

# ==================================================
# docker
# ==================================================
dc=`which docker-compose`

dc_check() {
  if [ -z "${dc}" ]; then
    echo "not exist docker-compose."
    exit 1
  fi
}

dc_command() {
  dc_check
  run_with_echo "$dc" "$@"
}

dc_run() {
  dc_command run --rm "$@"
}

dc_stop() {
  dc_command stop "$@"
}

dc_up() {
  dc_command up "$@"
}

dc_restart() {
  dc_stop
  dc_up "$@"
}

dc_restart_service() {
    service=$1
    shif
    dc_stop "$service"
    dc_up  "$service" "$@"
}