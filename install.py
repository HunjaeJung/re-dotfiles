#-*- encoding: utf-8 -*-
import os

tasks = {
    '~/.vimrc': 'vim/vimrc',
    '~/.vim': 'vim',
}

current_dir = os.path.abspath(os.path.dirname(__file__))

for target, source in tasks.items():

    # 현재 dir path에 붙이는 것
    source = os.path.join(current_dir, source)

    # User directory path에 붙이는 것
    target = os.path.expanduser(target)

    print source
    print target

    os.symlink(source, target)

