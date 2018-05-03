" /mnt/DATA/__programming/PROJECTS/config_tool/Session.vim:
" Vim session script.
" Created by session.vim 2.13.1 on 02 Mai 2018 at 23:45:15.
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
badd +452 tf_config.py
badd +4 validating_entry.py
badd +68 insert_dialog.py
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
exe 'vert 1resize ' . ((&columns * 25 + 64) / 128)
exe 'vert 2resize ' . ((&columns * 102 + 64) / 128)
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
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
16
silent! normal! zo
16
silent! normal! zo
40
silent! normal! zo
42
silent! normal! zo
52
silent! normal! zo
52
silent! normal! zo
55
silent! normal! zo
55
silent! normal! zo
57
silent! normal! zo
57
silent! normal! zo
58
silent! normal! zo
58
silent! normal! zo
61
silent! normal! zo
61
silent! normal! zo
64
silent! normal! zo
64
silent! normal! zo
66
silent! normal! zo
66
silent! normal! zo
72
silent! normal! zo
72
silent! normal! zo
80
silent! normal! zo
80
silent! normal! zo
81
silent! normal! zo
81
silent! normal! zo
85
silent! normal! zo
85
silent! normal! zo
88
silent! normal! zo
88
silent! normal! zo
100
silent! normal! zo
100
silent! normal! zo
107
silent! normal! zo
107
silent! normal! zo
114
silent! normal! zo
114
silent! normal! zo
117
silent! normal! zo
117
silent! normal! zo
122
silent! normal! zo
122
silent! normal! zo
125
silent! normal! zo
125
silent! normal! zo
127
silent! normal! zo
127
silent! normal! zo
129
silent! normal! zo
129
silent! normal! zo
132
silent! normal! zo
132
silent! normal! zo
134
silent! normal! zo
134
silent! normal! zo
139
silent! normal! zo
139
silent! normal! zo
142
silent! normal! zo
142
silent! normal! zo
145
silent! normal! zo
145
silent! normal! zo
149
silent! normal! zo
149
silent! normal! zo
153
silent! normal! zo
153
silent! normal! zo
156
silent! normal! zo
156
silent! normal! zo
157
silent! normal! zo
157
silent! normal! zo
159
silent! normal! zo
159
silent! normal! zo
52
silent! normal! zo
55
silent! normal! zo
57
silent! normal! zo
58
silent! normal! zo
61
silent! normal! zo
64
silent! normal! zo
66
silent! normal! zo
72
silent! normal! zo
80
silent! normal! zo
81
silent! normal! zo
85
silent! normal! zo
88
silent! normal! zo
100
silent! normal! zo
107
silent! normal! zo
114
silent! normal! zo
117
silent! normal! zo
122
silent! normal! zo
125
silent! normal! zo
127
silent! normal! zo
129
silent! normal! zo
132
silent! normal! zo
134
silent! normal! zo
139
silent! normal! zo
142
silent! normal! zo
145
silent! normal! zo
149
silent! normal! zo
153
silent! normal! zo
156
silent! normal! zo
157
silent! normal! zo
159
silent! normal! zo
163
silent! normal! zo
164
silent! normal! zo
177
silent! normal! zo
177
silent! normal! zo
180
silent! normal! zo
180
silent! normal! zo
180
silent! normal! zo
180
silent! normal! zo
183
silent! normal! zo
183
silent! normal! zo
183
silent! normal! zo
183
silent! normal! zo
186
silent! normal! zo
186
silent! normal! zo
186
silent! normal! zo
186
silent! normal! zo
193
silent! normal! zo
193
silent! normal! zo
193
silent! normal! zo
193
silent! normal! zo
180
silent! normal! zo
180
silent! normal! zo
183
silent! normal! zo
183
silent! normal! zo
186
silent! normal! zo
186
silent! normal! zo
193
silent! normal! zo
193
silent! normal! zo
201
silent! normal! zo
201
silent! normal! zo
204
silent! normal! zo
204
silent! normal! zo
218
silent! normal! zo
218
silent! normal! zo
219
silent! normal! zo
219
silent! normal! zo
222
silent! normal! zo
222
silent! normal! zo
224
silent! normal! zo
224
silent! normal! zo
230
silent! normal! zo
230
silent! normal! zo
231
silent! normal! zo
231
silent! normal! zo
234
silent! normal! zo
234
silent! normal! zo
234
silent! normal! zo
234
silent! normal! zo
236
silent! normal! zo
236
silent! normal! zo
239
silent! normal! zo
239
silent! normal! zo
239
silent! normal! zo
239
silent! normal! zo
243
silent! normal! zo
243
silent! normal! zo
244
silent! normal! zo
244
silent! normal! zo
246
silent! normal! zo
246
silent! normal! zo
248
silent! normal! zo
248
silent! normal! zo
252
silent! normal! zo
252
silent! normal! zo
201
silent! normal! zo
204
silent! normal! zo
218
silent! normal! zo
219
silent! normal! zo
222
silent! normal! zo
224
silent! normal! zo
230
silent! normal! zo
231
silent! normal! zo
234
silent! normal! zo
234
silent! normal! zo
236
silent! normal! zo
239
silent! normal! zo
239
silent! normal! zo
243
silent! normal! zo
244
silent! normal! zo
246
silent! normal! zo
248
silent! normal! zo
252
silent! normal! zo
256
silent! normal! zo
259
silent! normal! zo
268
silent! normal! zo
268
silent! normal! zo
269
silent! normal! zo
269
silent! normal! zo
272
silent! normal! zo
272
silent! normal! zo
276
silent! normal! zo
276
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
292
silent! normal! zo
292
silent! normal! zo
295
silent! normal! zo
295
silent! normal! zo
295
silent! normal! zo
295
silent! normal! zo
295
silent! normal! zo
302
silent! normal! zo
302
silent! normal! zo
303
silent! normal! zo
303
silent! normal! zo
303
silent! normal! zo
303
silent! normal! zo
306
silent! normal! zo
306
silent! normal! zo
308
silent! normal! zo
308
silent! normal! zo
310
silent! normal! zo
310
silent! normal! zo
313
silent! normal! zo
313
silent! normal! zo
319
silent! normal! zo
319
silent! normal! zo
328
silent! normal! zo
328
silent! normal! zo
332
silent! normal! zo
332
silent! normal! zo
335
silent! normal! zo
335
silent! normal! zo
336
silent! normal! zo
336
silent! normal! zo
338
silent! normal! zo
338
silent! normal! zo
340
silent! normal! zo
340
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
343
silent! normal! zo
343
silent! normal! zo
345
silent! normal! zo
345
silent! normal! zo
346
silent! normal! zo
346
silent! normal! zo
348
silent! normal! zo
348
silent! normal! zo
268
silent! normal! zo
269
silent! normal! zo
272
silent! normal! zo
276
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
280
silent! normal! zo
292
silent! normal! zo
295
silent! normal! zo
295
silent! normal! zo
302
silent! normal! zo
303
silent! normal! zo
303
silent! normal! zo
306
silent! normal! zo
308
silent! normal! zo
310
silent! normal! zo
313
silent! normal! zo
319
silent! normal! zo
328
silent! normal! zo
332
silent! normal! zo
335
silent! normal! zo
336
silent! normal! zo
338
silent! normal! zo
340
silent! normal! zo
341
silent! normal! zo
343
silent! normal! zo
345
silent! normal! zo
346
silent! normal! zo
348
silent! normal! zo
360
silent! normal! zo
361
silent! normal! zo
382
silent! normal! zo
382
silent! normal! zo
382
silent! normal! zo
382
silent! normal! zo
385
silent! normal! zo
385
silent! normal! zo
385
silent! normal! zo
385
silent! normal! zo
394
silent! normal! zo
394
silent! normal! zo
394
silent! normal! zo
394
silent! normal! zo
396
silent! normal! zo
396
silent! normal! zo
396
silent! normal! zo
396
silent! normal! zo
400
silent! normal! zo
400
silent! normal! zo
401
silent! normal! zo
401
silent! normal! zo
406
silent! normal! zo
406
silent! normal! zo
410
silent! normal! zo
410
silent! normal! zo
411
silent! normal! zo
411
silent! normal! zo
412
silent! normal! zo
412
silent! normal! zo
415
silent! normal! zo
415
silent! normal! zo
417
silent! normal! zo
417
silent! normal! zo
421
silent! normal! zo
421
silent! normal! zo
432
silent! normal! zo
432
silent! normal! zo
438
silent! normal! zo
438
silent! normal! zo
442
silent! normal! zo
442
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
382
silent! normal! zo
382
silent! normal! zo
385
silent! normal! zo
385
silent! normal! zo
394
silent! normal! zo
394
silent! normal! zo
396
silent! normal! zo
396
silent! normal! zo
400
silent! normal! zo
401
silent! normal! zo
406
silent! normal! zo
410
silent! normal! zo
411
silent! normal! zo
412
silent! normal! zo
415
silent! normal! zo
417
silent! normal! zo
421
silent! normal! zo
432
silent! normal! zo
438
silent! normal! zo
442
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
443
silent! normal! zo
448
silent! normal! zo
449
silent! normal! zo
455
silent! normal! zo
455
silent! normal! zo
457
silent! normal! zo
476
silent! normal! zo
476
silent! normal! zo
476
silent! normal! zo
476
silent! normal! zo
476
silent! normal! zo
476
silent! normal! zo
476
silent! normal! zo
482
silent! normal! zo
482
silent! normal! zo
495
silent! normal! zo
500
silent! normal! zo
502
silent! normal! zo
504
silent! normal! zo
506
silent! normal! zo
514
silent! normal! zo
514
silent! normal! zo
521
silent! normal! zo
521
silent! normal! zo
528
silent! normal! zo
528
silent! normal! zo
536
silent! normal! zo
536
silent! normal! zo
546
silent! normal! zo
546
silent! normal! zo
550
silent! normal! zo
550
silent! normal! zo
565
silent! normal! zo
565
silent! normal! zo
566
silent! normal! zo
566
silent! normal! zo
568
silent! normal! zo
568
silent! normal! zo
538
silent! normal! zo
546
silent! normal! zo
547
silent! normal! zo
549
silent! normal! zo
551
silent! normal! zo
553
silent! normal! zo
556
silent! normal! zo
560
silent! normal! zo
575
silent! normal! zo
576
silent! normal! zo
577
silent! normal! zo
579
silent! normal! zo
583
silent! normal! zo
584
silent! normal! zo
617
silent! normal! zo
617
silent! normal! zo
620
silent! normal! zo
620
silent! normal! zo
617
silent! normal! zo
620
silent! normal! zo
624
silent! normal! zo
let s:l = 478 - ((49 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
478
normal! 09|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 25 + 64) / 128)
exe 'vert 2resize ' . ((&columns * 102 + 64) / 128)
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
let s:l = 68 - ((46 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
68
normal! 0
tabedit validating_entry.py
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
let s:l = 71 - ((51 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
71
normal! 013|
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
1resize 60|vert 1resize 25|2resize 60|vert 2resize 102|
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
