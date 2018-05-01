" /mnt/DATA/__programming/PROJECTS/config_tool/Session.vim:
" Vim session script.
" Created by session.vim 2.13.1 on 01 Mai 2018 at 17:19:20.
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
let SuperTabCrMapping =  0 
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
badd +596 tf_config.py
argglobal
silent! argdel *
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
exe 'vert 1resize ' . ((&columns * 25 + 57) / 115)
exe 'vert 2resize ' . ((&columns * 89 + 57) / 115)
argglobal
enew
" file NERD_tree_1
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
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
235
silent! normal! zo
236
silent! normal! zo
273
silent! normal! zo
276
silent! normal! zo
302
silent! normal! zo
308
silent! normal! zo
324
silent! normal! zo
326
silent! normal! zo
326
silent! normal! zo
335
silent! normal! zo
339
silent! normal! zo
340
silent! normal! zo
348
silent! normal! zo
353
silent! normal! zo
363
silent! normal! zo
364
silent! normal! zo
365
silent! normal! zo
369
silent! normal! zo
372
silent! normal! zo
381
silent! normal! zo
382
silent! normal! zo
383
silent! normal! zo
417
silent! normal! zo
421
silent! normal! zo
421
silent! normal! zo
421
silent! normal! zo
421
silent! normal! zo
434
silent! normal! zo
437
silent! normal! zo
444
silent! normal! zo
452
silent! normal! zo
471
silent! normal! zo
503
silent! normal! zo
504
silent! normal! zo
581
silent! normal! zo
591
silent! normal! zo
592
silent! normal! zo
594
silent! normal! zo
597
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
620
silent! normal! zo
620
silent! normal! zo
627
silent! normal! zo
627
silent! normal! zo
631
silent! normal! zo
631
silent! normal! zo
644
silent! normal! zo
648
silent! normal! zo
652
silent! normal! zo
653
silent! normal! zo
686
silent! normal! zo
689
silent! normal! zo
693
silent! normal! zo
let s:l = 631 - ((30 * winheight(0) + 30) / 61)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
631
normal! 026|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 25 + 57) / 115)
exe 'vert 2resize ' . ((&columns * 89 + 57) / 115)
tabnext 1
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
1resize 61|vert 1resize 25|2resize 61|vert 2resize 89|
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
