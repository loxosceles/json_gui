" /mnt/DATA/__programming/PROJECTS/config_tool/Session.vim:
" Vim session script.
" Created by session.vim 2.13.1 on 30 Mai 2018 at 22:15:17.
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
31,50fold
53,54fold
55,65fold
67,75fold
77,79fold
81,83fold
85,87fold
89,91fold
92,109fold
110,139fold
140,172fold
173,223fold
224,229fold
230,246fold
247,249fold
250,260fold
261,271fold
272,296fold
297,310fold
311,311fold
311,313fold
314,314fold
314,318fold
314,318fold
52,318fold
321,359fold
360,374fold
375,379fold
380,397fold
398,416fold
417,431fold
432,440fold
441,449fold
320,449fold
452,453fold
454,464fold
465,472fold
473,523fold
524,559fold
451,559fold
561,561fold
562,581fold
582,599fold
600,609fold
610,620fold
621,639fold
640,648fold
561,648fold
651,661fold
662,686fold
687,739fold
740,754fold
755,792fold
793,799fold
650,799fold
801,801fold
802,806fold
807,831fold
832,851fold
852,860fold
801,860fold
862,862fold
863,897fold
898,900fold
901,904fold
905,907fold
908,911fold
912,915fold
862,915fold
862,916fold
917,926fold
52
silent! normal! zo
311
silent! normal! zo
311
normal! zc
314
silent! normal! zo
314
silent! normal! zo
314
normal! zc
320
silent! normal! zo
320
normal! zc
451
silent! normal! zo
524
silent! normal! zo
561
silent! normal! zo
582
silent! normal! zo
600
silent! normal! zo
610
silent! normal! zo
621
silent! normal! zo
650
silent! normal! zo
755
silent! normal! zo
801
silent! normal! zo
862
silent! normal! zo
862
silent! normal! zo
862
normal! zc
862
normal! zc
let s:l = 587 - ((34 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
587
normal! 09|
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
