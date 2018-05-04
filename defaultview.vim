let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
argglobal
if bufexists('/mnt/DATA/__programming/PROJECTS/config_tool/tf_config.py') | buffer /mnt/DATA/__programming/PROJECTS/config_tool/tf_config.py | else | edit /mnt/DATA/__programming/PROJECTS/config_tool/tf_config.py | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <expr> <C-Space> jedi#complete_string(0)
imap <buffer> <Nul> <C-Space>
xnoremap <buffer> ,r :call jedi#rename_visual()
snoremap <buffer> ,r :call jedi#rename_visual()
nnoremap <buffer> ,r :call jedi#rename()
nnoremap <buffer> ,n :call jedi#usages()
nnoremap <buffer> ,g :call jedi#goto_assignments()
nnoremap <buffer> ,d :call jedi#goto()
nnoremap <buffer> <silent> K :call jedi#show_documentation()
snoremap <buffer> <expr> <C-Space> 'c'.jedi#complete_string(0)
smap <buffer> <Nul> <C-Space>
inoremap <buffer> <silent>   =jedi#smart_auto_mappings()
inoremap <buffer> <silent> . .=jedi#complete_string(1)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=2
setlocal completefunc=youcompleteme#CompleteFunc
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=20
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=0{,0},:,!^F,o,O,e,<:>,=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=jedi#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en_us
setlocal statusline=%!airline#statusline(2)
setlocal suffixesadd=.py
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tags=
setlocal termkey=
setlocal termsize=
setlocal textwidth=85
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
16,16fold
16,16fold
31,31fold
31,31fold
31,31fold
31,31fold
31,31fold
31,31fold
31,33fold
31,33fold
43,50fold
76,76fold
92,92fold
86,98fold
101,101fold
100,101fold
79,101fold
113,113fold
104,123fold
134,134fold
126,138fold
150,150fold
141,152fold
166,166fold
168,168fold
164,168fold
171,171fold
173,173fold
155,175fold
178,184fold
187,193fold
196,202fold
206,206fold
210,210fold
214,214fold
216,216fold
213,216fold
40,216fold
234,234fold
234,234fold
237,237fold
237,237fold
240,240fold
240,240fold
243,243fold
243,243fold
250,250fold
250,250fold
221,254fold
261,272fold
258,275fold
285,285fold
288,288fold
290,292fold
278,293fold
303,303fold
306,306fold
306,306fold
311,311fold
311,311fold
308,312fold
296,312fold
325,325fold
323,325fold
327,327fold
315,327fold
331,337fold
220,337fold
344,350fold
354,355fold
357,358fold
353,358fold
365,368fold
365,368fold
365,368fold
365,368fold
380,380fold
380,381fold
388,388fold
388,388fold
391,391fold
393,393fold
395,396fold
398,398fold
404,404fold
387,406fold
377,406fold
361,406fold
417,417fold
421,421fold
423,423fold
420,423fold
426,426fold
428,428fold
425,428fold
431,431fold
433,433fold
430,433fold
413,441fold
341,441fold
446,463fold
469,470fold
469,470fold
478,478fold
478,478fold
480,480fold
480,480fold
466,481fold
466,481fold
485,488fold
490,490fold
484,491fold
499,499fold
501,502fold
496,502fold
495,502fold
494,502fold
505,522fold
530,530fold
530,530fold
530,530fold
530,530fold
530,530fold
530,530fold
530,530fold
530,530fold
529,530fold
525,531fold
445,531fold
536,541fold
551,553fold
558,561fold
558,561fold
558,561fold
558,561fold
558,561fold
558,561fold
558,561fold
564,564fold
564,564fold
544,566fold
575,575fold
577,577fold
579,579fold
581,581fold
589,589fold
589,589fold
596,596fold
596,596fold
603,603fold
603,603fold
570,608fold
619,619fold
621,621fold
618,621fold
623,623fold
625,625fold
627,627fold
630,631fold
633,633fold
611,641fold
646,646fold
648,648fold
645,648fold
644,648fold
535,648fold
653,682fold
685,685fold
688,688fold
691,692fold
652,692fold
695,703fold
40
normal! zo
43
normal! zc
79
normal! zo
86
normal! zo
92
normal! zc
86
normal! zc
100
normal! zo
101
normal! zc
100
normal! zc
79
normal! zc
104
normal! zo
113
normal! zc
104
normal! zc
126
normal! zo
134
normal! zc
126
normal! zc
141
normal! zo
150
normal! zc
141
normal! zc
155
normal! zo
164
normal! zo
166
normal! zc
168
normal! zc
164
normal! zc
171
normal! zc
173
normal! zc
155
normal! zc
178
normal! zc
187
normal! zc
196
normal! zc
206
normal! zc
210
normal! zc
213
normal! zo
214
normal! zc
216
normal! zc
213
normal! zc
220
normal! zo
221
normal! zo
234
normal! zo
234
normal! zc
234
normal! zc
237
normal! zo
237
normal! zc
237
normal! zc
240
normal! zo
240
normal! zc
240
normal! zc
243
normal! zo
243
normal! zc
243
normal! zc
250
normal! zo
250
normal! zc
250
normal! zc
221
normal! zc
258
normal! zo
258
normal! zc
278
normal! zo
278
normal! zc
296
normal! zo
308
normal! zo
308
normal! zc
296
normal! zc
315
normal! zo
323
normal! zo
315
normal! zc
331
normal! zc
341
normal! zo
344
normal! zc
353
normal! zo
354
normal! zc
357
normal! zc
353
normal! zc
361
normal! zo
365
normal! zo
365
normal! zo
365
normal! zo
365
normal! zc
365
normal! zc
365
normal! zc
365
normal! zc
377
normal! zo
380
normal! zo
380
normal! zc
387
normal! zo
387
normal! zc
377
normal! zc
361
normal! zc
413
normal! zo
420
normal! zo
420
normal! zc
413
normal! zc
445
normal! zo
446
normal! zc
466
normal! zo
466
normal! zo
469
normal! zo
469
normal! zc
469
normal! zc
466
normal! zc
466
normal! zc
484
normal! zo
485
normal! zc
484
normal! zc
494
normal! zo
495
normal! zo
496
normal! zo
496
normal! zc
495
normal! zc
494
normal! zc
525
normal! zo
529
normal! zo
530
normal! zo
530
normal! zo
530
normal! zo
530
normal! zo
530
normal! zo
530
normal! zo
530
normal! zo
525
normal! zc
535
normal! zo
536
normal! zc
544
normal! zo
551
normal! zc
558
normal! zo
558
normal! zo
558
normal! zo
558
normal! zo
558
normal! zo
558
normal! zo
544
normal! zc
570
normal! zo
577
normal! zc
579
normal! zc
581
normal! zc
570
normal! zc
611
normal! zo
618
normal! zo
621
normal! zc
618
normal! zc
623
normal! zc
625
normal! zc
627
normal! zc
611
normal! zc
644
normal! zo
645
normal! zo
648
normal! zc
645
normal! zc
644
normal! zc
652
normal! zo
653
normal! zc
691
normal! zc
695
normal! zc
let s:l = 543 - ((35 * winheight(0) + 30) / 60)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
543
normal! 0
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
" vim: set ft=vim :
