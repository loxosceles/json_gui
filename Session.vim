" /mnt/DATA/__programming/PROJECTS/config_tool/Session.vim:
" Vim session script.
" Created by session.vim 2.13.1 on 04 Mai 2018 at 01:48:29.
" Open this file in Vim and run :source % to restore your session.

set guioptions=aegimrLtT
silent! set guifont=
let &sessionoptions = 'blank,curdir,folds,help,options,tabpages,winsize,tabpages,globals'
let g:session_autoload = 'yes'
let g:session_autosave = 'yes'
let g:session_autosave_periodic = 1
if exists('g:syntax_on') != 1 | syntax on | endif
if exists('g:did_load_filetypes') != 1 | filetype on | endif
if exists('g:did_load_ftplugin') != 1 | filetype plugin on | endif
if exists('g:did_indent_on') != 1 | filetype indent on | endif
if &background != 'light'
	set background=light
endif
call setqflist([])
let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
let NERDTreeMapPreviewSplit = "gi"
let NERDTreeMapCloseChildren = "X"
let NERDTreeShowHidden =  1 
let EasyMotion_off_screen_search =  1 
let SuperTabDefaultCompletionType = "<C-n>"
let UltiSnipsUsePythonVersion =  3 
let SuperTabLongestHighlight =  0 
let NERDTreeMapCloseDir = "x"
let NERDTreeSortHiddenFirst = "1"
let NERDTreeMarkBookmarks = "1"
let NERDUsePlaceHolders = "1"
let NERDTreeShowLineNumbers = "0"
let UltiSnipsExpandTrigger = "<tab>"
let NERDTreeRespectWildIgnore = "0"
let NERDTreeAutoDeleteBuffer =  0 
let EasyMotion_smartcase =  0 
let SuperTabUndoBreak =  0 
let NERDTreeBookmarksFile = "/home/arytloc/.NERDTreeBookmarks"
let UltiSnipsJumpForwardTrigger = "<tab>"
let NERDTreeMapToggleHidden = "I"
let NERDTreeWinSize =  25 
let EasyMotion_enter_jump_first =  0 
let EasyMotion_use_upper =  0 
let EasyMotion_do_mapping =  1 
let SuperTabCrMapping =  1 
let SuperTabCompleteCase = "inherit"
let SuperTabClosePreviewOnPopupClose =  0 
let NERDTreeMapPreview = "go"
let UltiSnipsRemoveSelectModeMappings =  1 
let NERDTreeCascadeSingleChildDir = "1"
let Taboo_tabs = ""
let NERDTreeNotificationThreshold = "100"
let NERDTreeMapActivateNode = "o"
let NERDTreeWinPos = "left"
let NERDTreeDirArrowExpandable = "▸"
let NERDCommentEmptyLines =  1 
let EasyMotion_disable_two_key_combo =  0 
let NERDTreeMapMenu = "m"
let EasyMotion_space_jump_first =  0 
let EasyMotion_prompt = "Search for {n} character(s): "
let EasyMotion_use_regexp =  1 
let NERDTreeMapOpenInTabSilent = "T"
let NERDTreeMapHelp = "?"
let EasyMotion_move_highlight =  1 
let NERDTreeMapJumpParent = "p"
let NERDTreeMapToggleFilters = "f"
let SuperTabMappingForward = "<tab>"
let NERDTreeAutoCenter = "1"
let SuperTabContextDefaultCompletionType = "<c-p>"
let NERDTreeMapJumpPrevSibling = "<C-k>"
let NERDTreeShowBookmarks = "0"
let NERDMenuMode = "3"
let NERDTreeRemoveDirCmd = "rm -rf "
let NERDRemoveExtraSpaces = "0"
let NERDTreeMapOpenInTab = "t"
let EasyMotion_show_prompt =  1 
let EasyMotion_add_search_history =  1 
let NERDTreeChDirMode = "0"
let EasyMotion_do_shade =  1 
let NERDTreeCreatePrefix = "silent"
let NERDTreeMinimalUI = "0"
let EasyMotion_grouping =  1 
let NERDTreeAutoCenterThreshold = "3"
let NERDTreeShowFiles = "1"
let NERDTreeMapOpenSplit = "i"
let EasyMotion_skipfoldedline =  1 
let NERDTreeCaseSensitiveSort = "0"
let NERDTreeHijackNetrw = "1"
let NERDSpaceDelims =  1 
let SuperTabMappingTabLiteral = "<C-v>"
let NERDTreeMapRefresh = "r"
let NERDTreeBookmarksSort = "1"
let NERDTreeHighlightCursorline = "1"
let UltiSnipsEnableSnipMate =  1 
let NERDLPlace = "[>"
let EasyMotion_use_migemo =  0 
let NERDDefaultAlign = "left"
let NERDTreeMouseMode = "1"
let NERDCreateDefaultMappings = "1"
let NERDTreeMapCWD = "CD"
let NERDTreeNaturalSort = "0"
let EasyMotion_verbose =  1 
let NERDTreeMapPreviewVSplit = "gs"
let NERDTreeMapUpdir = "u"
let NERDTreeMapJumpRoot = "P"
let NERDCommentWholeLinesInVMode = "0"
let UltiSnipsJumpBackwardTrigger = "<s-tab>"
let NERDTreeGlyphReadOnly = "RO"
let NERDTreeMapChdir = "cd"
let NERDRPlace = "<]"
let NERDTreeMapToggleZoom = "A"
let NERDDefaultNesting = "1"
let NERDTreeMapRefreshRoot = "R"
let EasyMotion_cursor_highlight =  1 
let NERDRemoveAltComs = "1"
let NERDTreeCascadeOpenSingleChildDir = "1"
let NERDTreeMapOpenVSplit = "s"
let NERDTreeMapJumpLastChild = "J"
let SuperTabLongestEnhanced =  0 
let NERDTrimTrailingWhitespace =  1 
let NERDTreeMapDeleteBookmark = "D"
let UltiSnipsListSnippets = "<c-tab>"
let NERDBlockComIgnoreEmpty = "0"
let EasyMotion_startofline =  1 
let NERDTreeMapJumpNextSibling = "<C-j>"
let EasyMotion_inc_highlight =  1 
let UltiSnipsEditSplit = "normal"
let NERDTreeCopyCmd = "cp -r "
let SuperTabRetainCompletionDuration = "insert"
let NERDTreeMapQuit = "q"
let NERDTreeMapChangeRoot = "C"
let NERDCompactSexyComs =  1 
let NERDTreeSortDirs = "1"
let NERDTreeMapToggleFiles = "F"
let EasyMotion_keys = "asdghklqwertyuiopzxcvbnmfj;"
let NERDAllowAnyVisualDelims = "1"
let EasyMotion_force_csapprox =  0 
let EasyMotion_loaded =  1 
let NERDTreeMapOpenExpl = "e"
let NERDTreeMapJumpFirstChild = "K"
let NERDTreeDirArrowCollapsible = "▾"
let NERDTreeMapOpenRecursively = "O"
let NERDTreeMapToggleBookmarks = "B"
let SuperTabMappingBackward = "<s-tab>"
let NERDTreeMapUpdirKeepOpen = "U"
let EasyMotion_landing_highlight =  0 
let NERDTreeQuitOnOpen = "0"
let NERDTreeStatusline = "%{exists('b:NERDTree')?b:NERDTree.root.path.str():''}"
silent only
cd /mnt/DATA/__programming/PROJECTS/config_tool
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +365 tf_config.py
badd +89 insert_dialog.py
argglobal
silent! argdel *
set stal=2
edit tf_config.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winheight=1 winminwidth=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 25 + 61) / 123)
exe 'vert 2resize ' . ((&columns * 97 + 61) / 123)
argglobal
enew
" file NERD_tree_2
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
wincmd w
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=20
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
17,17fold
17,17fold
17,17fold
4,19fold
20,38fold
43,52fold
54,63fold
65,67fold
69,71fold
73,75fold
77,79fold
80,95fold
96,120fold
121,142fold
143,157fold
158,171fold
172,194fold
195,203fold
204,212fold
213,221fold
222,233fold
234,236fold
40,236fold
239,273fold
274,298fold
299,316fold
317,335fold
336,350fold
351,359fold
238,359fold
364,372fold
364,373fold
374,381fold
382,430fold
431,466fold
361,466fold
469,488fold
507,516fold
517,527fold
528,552fold
553,561fold
469,561fold
562,568fold
468,568fold
571,578fold
579,603fold
604,645fold
646,679fold
680,686fold
570,686fold
689,720fold
721,723fold
724,727fold
728,730fold
731,731fold
731,734fold
688,734fold
736,745fold
4
silent! normal! zo
17
silent! normal! zo
17
silent! normal! zo
17
normal! zc
4
normal! zc
20
normal! zc
40
silent! normal! zo
43
normal! zc
54
normal! zc
65
normal! zc
69
normal! zc
73
normal! zc
77
normal! zc
80
normal! zc
96
normal! zc
121
normal! zc
143
normal! zc
158
normal! zc
172
normal! zc
195
normal! zc
204
normal! zc
213
normal! zc
222
normal! zc
234
normal! zc
40
normal! zc
238
silent! normal! zo
239
normal! zc
299
normal! zc
317
normal! zc
351
normal! zc
361
silent! normal! zo
364
silent! normal! zo
364
normal! zc
374
normal! zc
382
normal! zc
431
normal! zc
361
normal! zc
468
silent! normal! zo
469
silent! normal! zo
469
normal! zc
507
normal! zc
517
normal! zc
528
normal! zc
553
normal! zc
562
normal! zc
468
normal! zc
570
silent! normal! zo
571
normal! zc
579
normal! zc
604
normal! zc
646
normal! zc
680
normal! zc
570
normal! zc
688
silent! normal! zo
689
normal! zc
721
normal! zc
724
normal! zc
728
normal! zc
731
silent! normal! zo
731
normal! zc
731
normal! zc
688
normal! zc
736
normal! zc
let s:l = 338 - ((337 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
338
normal! 0
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 25 + 61) / 123)
exe 'vert 2resize ' . ((&columns * 97 + 61) / 123)
tabedit insert_dialog.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winheight=1 winminwidth=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
7,41fold
43,47fold
49,66fold
68,79fold
81,88fold
90,92fold
94,96fold
5,96fold
5
silent! normal! zo
let s:l = 1 - ((0 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
tabnext 1
set stal=1
if exists('s:wipebuf')
"   silent exe 'bwipe ' . s:wipebuf
endif
" unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOc
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save

" Support for special windows like quick-fix and plug-in windows.
" Everything down here is generated by vim-session (not supported
" by :mksession out of the box).

1wincmd w
tabnext 1
let s:bufnr_save = bufnr("%")
let s:cwd_save = getcwd()
NERDTree /mnt/DATA/__programming/PROJECTS/config_tool
if !getbufvar(s:bufnr_save, '&modified')
  let s:wipebuflines = getbufline(s:bufnr_save, 1, '$')
  if len(s:wipebuflines) <= 1 && empty(get(s:wipebuflines, 0, ''))
    silent execute 'bwipeout' s:bufnr_save
  endif
endif
execute "cd" fnameescape(s:cwd_save)
1resize 60|vert 1resize 25|2resize 60|vert 2resize 97|
2wincmd w
tabnext 1
if exists('s:wipebuf')
  if empty(bufname(s:wipebuf))
if !getbufvar(s:wipebuf, '&modified')
  let s:wipebuflines = getbufline(s:wipebuf, 1, '$')
  if len(s:wipebuflines) <= 1 && empty(get(s:wipebuflines, 0, ''))
    silent execute 'bwipeout' s:wipebuf
  endif
endif
  endif
endif
doautoall SessionLoadPost
unlet SessionLoad
" vim: ft=vim ro nowrap smc=128
