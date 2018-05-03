" /mnt/DATA/__programming/PROJECTS/config_tool/Session.vim:
" Vim session script.
" Created by session.vim 2.13.1 on 03 Mai 2018 at 15:01:01.
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
badd +1 tf_config.py
badd +0 insert_dialog.py
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
setlocal fdl=20
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
16,16fold
16,16fold
16,16fold
16,16fold
21,34fold
45,51fold
45,51fold
61,61fold
61,61fold
72,73fold
72,73fold
71,73fold
71,73fold
70,73fold
70,73fold
89,89fold
89,89fold
84,95fold
84,95fold
98,98fold
98,98fold
97,98fold
97,98fold
82,98fold
82,98fold
110,110fold
110,110fold
107,120fold
107,120fold
131,131fold
131,131fold
125,135fold
125,135fold
147,147fold
147,147fold
144,149fold
144,149fold
163,163fold
163,163fold
165,165fold
165,165fold
161,165fold
161,165fold
168,168fold
168,168fold
170,170fold
170,170fold
158,172fold
158,172fold
181,181fold
181,181fold
190,190fold
190,190fold
199,199fold
199,199fold
203,203fold
203,203fold
207,207fold
207,207fold
211,211fold
211,211fold
213,213fold
213,213fold
210,213fold
210,213fold
41,213fold
41,213fold
231,231fold
231,231fold
231,231fold
231,231fold
234,234fold
234,234fold
234,234fold
234,234fold
237,237fold
237,237fold
237,237fold
237,237fold
240,240fold
240,240fold
240,240fold
240,240fold
247,247fold
247,247fold
247,247fold
247,247fold
218,251fold
218,251fold
260,272fold
260,272fold
257,275fold
257,275fold
279,279fold
279,279fold
282,282fold
282,282fold
284,286fold
284,286fold
278,287fold
278,287fold
291,291fold
291,291fold
294,294fold
294,294fold
294,294fold
294,294fold
299,299fold
299,299fold
299,299fold
299,299fold
296,300fold
296,300fold
290,300fold
290,300fold
306,306fold
306,306fold
304,306fold
304,306fold
308,308fold
308,308fold
303,308fold
303,308fold
312,312fold
312,312fold
217,312fold
217,312fold
319,326fold
319,326fold
318,326fold
330,331fold
330,331fold
333,334fold
333,334fold
329,334fold
329,334fold
341,344fold
341,344fold
341,344fold
341,344fold
341,344fold
341,344fold
341,344fold
341,344fold
341,344fold
355,355fold
355,355fold
355,356fold
355,356fold
355,356fold
363,363fold
363,363fold
363,363fold
363,363fold
366,366fold
366,366fold
368,368fold
368,368fold
370,371fold
370,371fold
373,373fold
373,373fold
379,379fold
379,379fold
362,381fold
362,381fold
352,381fold
352,381fold
337,381fold
337,381fold
392,392fold
392,392fold
396,396fold
396,396fold
398,398fold
398,398fold
395,398fold
395,398fold
401,401fold
401,401fold
403,403fold
403,403fold
400,403fold
400,403fold
406,406fold
406,406fold
408,408fold
408,408fold
405,408fold
405,408fold
388,416fold
388,416fold
316,416fold
316,416fold
421,438fold
421,438fold
445,446fold
445,446fold
445,446fold
445,446fold
454,454fold
454,454fold
454,454fold
454,454fold
456,456fold
456,456fold
456,456fold
456,456fold
442,457fold
442,457fold
442,457fold
442,457fold
461,464fold
461,464fold
466,466fold
466,466fold
460,467fold
460,467fold
475,475fold
475,475fold
477,478fold
477,478fold
472,478fold
472,478fold
471,478fold
471,478fold
470,478fold
470,478fold
481,501fold
481,501fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
509,509fold
508,509fold
508,509fold
504,510fold
504,510fold
420,510fold
420,510fold
516,521fold
516,521fold
531,533fold
531,533fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
538,541fold
544,544fold
544,544fold
544,544fold
544,544fold
524,546fold
524,546fold
557,557fold
557,557fold
559,559fold
559,559fold
561,561fold
561,561fold
563,563fold
563,563fold
573,573fold
573,573fold
573,573fold
573,573fold
580,580fold
580,580fold
580,580fold
580,580fold
587,587fold
587,587fold
587,587fold
587,587fold
552,592fold
552,592fold
604,604fold
604,604fold
606,606fold
606,606fold
603,606fold
603,606fold
608,608fold
608,608fold
610,610fold
610,610fold
612,612fold
612,612fold
615,616fold
615,616fold
618,618fold
618,618fold
596,624fold
596,624fold
626,626fold
626,626fold
628,628fold
628,628fold
625,628fold
625,628fold
620,623fold
625,628fold
514,628fold
514,628fold
633,651fold
633,651fold
658,658fold
658,658fold
661,662fold
661,662fold
632,662fold
632,662fold
665,672fold
665,672fold
16
silent! normal! zo
16
silent! normal! zo
16
silent! normal! zo
41
silent! normal! zo
41
silent! normal! zo
45
silent! normal! zo
61
silent! normal! zo
70
silent! normal! zo
70
silent! normal! zo
71
silent! normal! zo
71
silent! normal! zo
72
silent! normal! zo
82
silent! normal! zo
82
silent! normal! zo
84
silent! normal! zo
84
silent! normal! zo
89
silent! normal! zo
97
silent! normal! zo
97
silent! normal! zo
98
silent! normal! zo
107
silent! normal! zo
107
silent! normal! zo
110
silent! normal! zo
125
silent! normal! zo
125
silent! normal! zo
131
silent! normal! zo
144
silent! normal! zo
144
silent! normal! zo
147
silent! normal! zo
158
silent! normal! zo
158
silent! normal! zo
161
silent! normal! zo
161
silent! normal! zo
163
silent! normal! zo
165
silent! normal! zo
168
silent! normal! zo
170
silent! normal! zo
181
silent! normal! zo
190
silent! normal! zo
199
silent! normal! zo
203
silent! normal! zo
207
silent! normal! zo
210
silent! normal! zo
210
silent! normal! zo
211
silent! normal! zo
213
silent! normal! zo
217
silent! normal! zo
217
silent! normal! zo
218
silent! normal! zo
218
silent! normal! zo
231
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
237
silent! normal! zo
237
silent! normal! zo
237
silent! normal! zo
240
silent! normal! zo
240
silent! normal! zo
240
silent! normal! zo
247
silent! normal! zo
247
silent! normal! zo
247
silent! normal! zo
257
silent! normal! zo
257
silent! normal! zo
260
silent! normal! zo
278
silent! normal! zo
278
silent! normal! zo
279
silent! normal! zo
282
silent! normal! zo
284
silent! normal! zo
290
silent! normal! zo
290
silent! normal! zo
291
silent! normal! zo
294
silent! normal! zo
294
silent! normal! zo
294
silent! normal! zo
296
silent! normal! zo
296
silent! normal! zo
299
silent! normal! zo
299
silent! normal! zo
299
silent! normal! zo
303
silent! normal! zo
303
silent! normal! zo
304
silent! normal! zo
304
silent! normal! zo
306
silent! normal! zo
308
silent! normal! zo
312
silent! normal! zo
316
silent! normal! zo
316
silent! normal! zo
318
silent! normal! zo
319
silent! normal! zo
329
silent! normal! zo
329
silent! normal! zo
330
silent! normal! zo
333
silent! normal! zo
337
silent! normal! zo
337
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
341
silent! normal! zo
352
silent! normal! zo
352
silent! normal! zo
355
silent! normal! zo
355
silent! normal! zo
355
silent! normal! zo
355
silent! normal! zo
362
silent! normal! zo
362
silent! normal! zo
363
silent! normal! zo
363
silent! normal! zo
363
silent! normal! zo
366
silent! normal! zo
368
silent! normal! zo
370
silent! normal! zo
373
silent! normal! zo
379
silent! normal! zo
388
silent! normal! zo
388
silent! normal! zo
392
silent! normal! zo
395
silent! normal! zo
395
silent! normal! zo
396
silent! normal! zo
398
silent! normal! zo
400
silent! normal! zo
400
silent! normal! zo
401
silent! normal! zo
403
silent! normal! zo
405
silent! normal! zo
405
silent! normal! zo
406
silent! normal! zo
408
silent! normal! zo
420
silent! normal! zo
420
silent! normal! zo
421
silent! normal! zo
442
silent! normal! zo
442
silent! normal! zo
442
silent! normal! zo
442
silent! normal! zo
445
silent! normal! zo
445
silent! normal! zo
445
silent! normal! zo
454
silent! normal! zo
454
silent! normal! zo
454
silent! normal! zo
456
silent! normal! zo
456
silent! normal! zo
456
silent! normal! zo
460
silent! normal! zo
460
silent! normal! zo
461
silent! normal! zo
466
silent! normal! zo
470
silent! normal! zo
470
silent! normal! zo
471
silent! normal! zo
471
silent! normal! zo
472
silent! normal! zo
472
silent! normal! zo
475
silent! normal! zo
477
silent! normal! zo
481
silent! normal! zo
504
silent! normal! zo
504
silent! normal! zo
508
silent! normal! zo
508
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
509
silent! normal! zo
514
silent! normal! zo
514
silent! normal! zo
516
silent! normal! zo
524
silent! normal! zo
524
silent! normal! zo
531
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
538
silent! normal! zo
544
silent! normal! zo
544
silent! normal! zo
544
silent! normal! zo
552
silent! normal! zo
552
silent! normal! zo
557
silent! normal! zo
559
silent! normal! zo
561
silent! normal! zo
563
silent! normal! zo
573
silent! normal! zo
573
silent! normal! zo
573
silent! normal! zo
580
silent! normal! zo
580
silent! normal! zo
580
silent! normal! zo
587
silent! normal! zo
587
silent! normal! zo
587
silent! normal! zo
596
silent! normal! zo
596
silent! normal! zo
603
silent! normal! zo
603
silent! normal! zo
604
silent! normal! zo
606
silent! normal! zo
608
silent! normal! zo
610
silent! normal! zo
612
silent! normal! zo
615
silent! normal! zo
618
silent! normal! zo
625
silent! normal! zo
620
silent! normal! zo
625
silent! normal! zo
625
silent! normal! zo
626
silent! normal! zo
628
silent! normal! zo
632
silent! normal! zo
632
silent! normal! zo
633
silent! normal! zo
658
silent! normal! zo
661
silent! normal! zo
665
silent! normal! zo
let s:l = 652 - ((0 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
652
normal! 0
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
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
7
silent! normal! zo
9
silent! normal! zo
52
silent! normal! zo
69
silent! normal! zo
70
silent! normal! zo
83
silent! normal! zo
let s:l = 95 - ((59 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
95
normal! 09|
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
