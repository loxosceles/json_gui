" /mnt/DATA/__programming/PROJECTS/config_tool/Session.vim:
" Vim session script.
" Created by session.vim 2.13.1 on 31 Mai 2018 at 00:06:09.
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
let NERDTreeMinimalUI = "0"
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
let NERDTreeStatusline = "%{matchstr(getline('.'), '\\s\\zs\\w\\(.*\\)')}"
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
let EasyMotion_grouping =  1 
let NERDTreeAutoCenterThreshold = "3"
let NERDTreeShowFiles = "1"
let NERDTreeMapOpenSplit = "i"
let NERDTreeDirArrowCollapsible = "▾"
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
let NERDTreeMapOpenRecursively = "O"
let NERDTreeMapToggleBookmarks = "B"
let SuperTabMappingBackward = "<s-tab>"
let NERDTreeMapUpdirKeepOpen = "U"
let EasyMotion_landing_highlight =  0 
let NERDTreeQuitOnOpen = "0"
silent only
cd /mnt/DATA/__programming/PROJECTS/config_tool
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +460 tf_config.py
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
exe 'vert 1resize ' . ((&columns * 25 + 53) / 107)
exe 'vert 2resize ' . ((&columns * 81 + 53) / 107)
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
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
1,2fold
4,30fold
31,49fold
52,53fold
54,64fold
66,74fold
76,78fold
80,82fold
84,86fold
88,90fold
91,108fold
109,143fold
144,173fold
174,206fold
207,257fold
258,263fold
264,270fold
271,273fold
274,284fold
285,309fold
310,323fold
324,324fold
324,326fold
327,327fold
327,331fold
327,331fold
51,331fold
332,341fold
342,352fold
353,363fold
366,404fold
405,421fold
422,426fold
427,445fold
446,464fold
465,480fold
481,489fold
490,498fold
365,498fold
501,502fold
503,513fold
514,521fold
522,572fold
573,577fold
500,577fold
579,579fold
580,598fold
600,600fold
599,616fold
617,629fold
632,642fold
643,667fold
668,720fold
721,735fold
736,774fold
775,781fold
631,781fold
783,783fold
784,788fold
789,813fold
814,830fold
831,839fold
783,839fold
841,841fold
842,876fold
877,879fold
880,883fold
884,886fold
887,890fold
891,894fold
841,894fold
841,894fold
896,905fold
51
silent! normal! zo
324
silent! normal! zo
324
normal! zc
327
silent! normal! zo
327
silent! normal! zo
327
normal! zc
365
silent! normal! zo
405
silent! normal! zo
500
silent! normal! zo
503
silent! normal! zo
599
silent! normal! zo
599
normal! zc
631
silent! normal! zo
736
silent! normal! zo
783
silent! normal! zo
783
normal! zc
841
silent! normal! zo
841
silent! normal! zo
841
normal! zc
let s:l = 741 - ((238 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
741
normal! 016|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 25 + 53) / 107)
exe 'vert 2resize ' . ((&columns * 81 + 53) / 107)
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
1resize 42|vert 1resize 25|2resize 42|vert 2resize 81|
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
