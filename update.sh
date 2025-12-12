#!/bin/bash

# 自动切到脚本所在目录（保证总是对的）
SCRIPT_PATH="$(
  cd "$(dirname "$0")" || exit
  pwd -P
)"
cd "$SCRIPT_PATH" || exit

echo "📂 当前路径: $(pwd)"



# 获取当前分支
branch=$(git rev-parse --abbrev-ref HEAD)

# 检查未跟踪文件（untracked）
if [ -n "$(git ls-files --others --exclude-standard)" ]; then
  echo "📄 检测到新的未跟踪文件，将一并提交～"
  git add .
else
  # 如果没有新文件，只 add 修改过的
  git add -u
fi

# 再次确认是否有改动（包括暂存区）
if git diff --cached --quiet; then
  echo "🌼 没有检测到需要提交的改动噢～✨"
  exit 0
fi

# 提示输入 commit 信息
echo "🪶 请输入 commit message（直接回车则使用默认：chore: quick save）："
read msg

# 如果用户直接回车
if [ -z "$msg" ]; then
  msg="chore: quick save"
fi

# 提交并推送
git add .
git commit -m "$msg"
git push origin "$branch"
# git push --force origin "$branch"
# 输出结果提示
echo -e "\n🌸 提交成功到分支 ➜ \033[1;32m$branch\033[0m 💚"
echo "💬 提交信息：$msg"