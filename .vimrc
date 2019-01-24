execute pathogen#infect()

set rtp+=~/.fzf

syntax enable
let g:python_highlight_all = 1
let g:jedi#auto_vim_configuration = 0
let g:jedi#popup_on_dot = 0
let g:jedi#popup_select_first = 0
let g:jedi#use_tabs_not_buffers = 0
let g:jedi#use_splits_not_buffers = "bottom"

" Challenger Deep Colorscheme stuff
"colorscheme challenger_deep
"if has('nvim') || has('termguicolors')
"  set termguicolors
"endif
"let g:lightline = { 'colorscheme': 'challenger_deep'}

" ---------------------------------------------------

set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4

set number
set showcmd
filetype indent on
set cursorline
set showmatch

set incsearch
set hlsearch

set background=dark
set foldenable
set foldlevelstart=10
set foldnestmax=10
nnoremap <space> za
set foldmethod=indent

"Move vertically by visual line
nnoremap j gj
nnoremap k gk

"Move to beginning/end of line
nnoremap B ^
nnoremap E $

"$/^ doesnt do anything
nnoremap $ <nop>
nnoremap ^ <nop>

"Visually selects the last inserted texts
nnoremap gV '[v']

let mapleader="," "leader is Comma

" jk is escape
inoremap jk <esc>

"toggle gundo
nnoremap <leader>u :GundoToggle<CR>

