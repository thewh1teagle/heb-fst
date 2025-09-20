============================= test session starts ==============================
platform darwin -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/yqbqwlny/Documents/audio/heb-fst
configfile: pyproject.toml
collected 278 items

tests/test_phonemize.py .......F..F..F.FF.F..F...F....F.....F..F..FFFFFF [ 17%]
F...F.F....FFFFF..FF.FFF..FFFFFFF.F.F...F.F..FF.F...FF.F..F.FFF.FFF.F... [ 43%]
F.FF.FFFF.F.F.FF..FF.F.F..FFFFFFFFF.FFFFFFFFFFFFFFFFFFFF..F..FFFFFFFFFFF [ 69%]
FFFFFFFFFF...F.FFFFFFF.F..F.FFF.....FFF...F...FF.FFFFFFFFFFFFF..FFFFFFFF [ 94%]
F.FFFFF.FFFFFF                                                           [100%]

=================================== FAILURES ===================================
______________ test_phonemize[\u05db\u05bc\u05c7\u05dc-k\u02c8ol] ______________

word = 'כׇּל', expected = 'kˈol'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כׇּל: got xˈol, expected kˈol
E       assert 'xˈol' == 'kˈol'
E         
E         - kˈol
E         ? ^
E         + xˈol
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d9\u05b4\u05e9\u05c2\u05b0\u05e8\u05b8\u05d0\u05b5\u05dc-jisra\u0294\u02c8el] _

word = 'יִשְׂרָאֵל', expected = 'jisraʔˈel'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: יִשְׂרָאֵל: got jiʃraʔˈel, expected jisraʔˈel
E       assert 'jiʃraʔˈel' == 'jisraʔˈel'
E         
E         - jisraʔˈel
E         ?   ^
E         + jiʃraʔˈel
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e8\u05b7\u05db\u05b6\u05bc\u05ab\u05d1\u05b6\u05dc-rak\u02c8evel] _

word = 'רַכֶּ֫בֶל', expected = 'rakˈevel'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רַכֶּ֫בֶל: got raxˈevel, expected rakˈevel
E       assert 'raxˈevel' == 'rakˈevel'
E         
E         - rakˈevel
E         ?   ^
E         + raxˈevel
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e8\u05b5\u05ab\u05d9\u05d7\u05b7-r\u02c8eax] ________

word = 'רֵ֫יחַ', expected = 'rˈeax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רֵ֫יחַ: got rˈejax, expected rˈeax
E       assert 'rˈejax' == 'rˈeax'
E         
E         - rˈeax
E         + rˈejax
E         ?    +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05d1\u05b7\u05bc\u05ab\u05d9\u05b4\u05ea-b\u02c8ajit] ____

word = 'בַּ֫יִת', expected = 'bˈajit'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בַּ֫יִת: got vˈajit, expected bˈajit
E       assert 'vˈajit' == 'bˈajit'
E         
E         - bˈajit
E         ? ^
E         + vˈajit
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e9\u05c2\u05b7\u05ab\u05de\u05b0\u05ea\u05bc\u05b8-s\u02c8amta] _

word = 'שַׂ֫מְתָּ', expected = 'sˈamta'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שַׂ֫מְתָּ: got ʃˈamta, expected sˈamta
E       assert 'ʃˈamta' == 'sˈamta'
E         
E         - sˈamta
E         ? ^
E         + ʃˈamta
E         ? ^

tests/test_phonemize.py:16: AssertionError
___________ test_phonemize[\u05db\u05b8\u05bc\u05d0\u05df-k\u02c8an] ___________

word = 'כָּאן', expected = 'kˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כָּאן: got xˈaʔn, expected kˈan
E       assert 'xˈaʔn' == 'kˈan'
E         
E         - kˈan
E         + xˈaʔn

tests/test_phonemize.py:16: AssertionError
___ test_phonemize[\u05e6\u05b7\u05d5\u05b7\u05bc\u05d0\u05e8-tsav\u02c8ar] ____

word = 'צַוַּאר', expected = 'tsavˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צַוַּאר: got tsavˈaʔr, expected tsavˈar
E       assert 'tsavˈaʔr' == 'tsavˈar'
E         
E         - tsavˈar
E         + tsavˈaʔr
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b4\u05d5\u05b0\u05d9\u05b8\u05ea\u05b8\u05df-livjat\u02c8an0] _

word = 'לִוְיָתָן', expected = 'livjatˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִוְיָתָן: got liujatˈan, expected livjatˈan
E       assert 'liujatˈan' == 'livjatˈan'
E         
E         - livjatˈan
E         ?   ^
E         + liujatˈan
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05bc\u05b8\u05d0\u05b2\u05d1\u05b8\u05d4-ka\u0294av\u02c8a] _

word = 'כָּאֲבָה', expected = 'kaʔavˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כָּאֲבָה: got xaʔavˈa, expected kaʔavˈa
E       assert 'xaʔavˈa' == 'kaʔavˈa'
E         
E         - kaʔavˈa
E         ? ^
E         + xaʔavˈa
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b4\u05e1\u05b0\u05e2\u05b4\u05ab\u05d9\u05e8\u05d5\u05bc-his\u0294\u02c8iru] _

word = 'הִסְעִ֫ירוּ', expected = 'hisʔˈiru'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הִסְעִ֫ירוּ: got hisʔˈijrv, expected hisʔˈiru
E       assert 'hisʔˈijrv' == 'hisʔˈiru'
E         
E         - hisʔˈiru
E         ?        ^
E         + hisʔˈijrv
E         ?       + ^

tests/test_phonemize.py:16: AssertionError
______________ test_phonemize[\u05d6\u05b9\u05d0\u05ea-z\u02c8ot] ______________

word = 'זֹאת', expected = 'zˈot'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: זֹאת: got zˈoʔt, expected zˈot
E       assert 'zˈoʔt' == 'zˈot'
E         
E         - zˈot
E         + zˈoʔt
E         ?    +

tests/test_phonemize.py:16: AssertionError
__ test_phonemize[\u05e8\u05b8\u05d0\u05e9\u05c1\u05b4\u05d9-ra\u0283\u02c8i] __

word = 'רָאשִׁי', expected = 'raʃˈi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רָאשִׁי: got raʔʃˈi, expected raʃˈi
E       assert 'raʔʃˈi' == 'raʃˈi'
E         
E         - raʃˈi
E         + raʔʃˈi
E         ?   +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b8\u05e2\u05b2\u05e8\u05d5\u05bc-ba\u0294ar\u02c8u] _

word = 'בָּעֲרוּ', expected = 'baʔarˈu'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בָּעֲרוּ: got vaʔˈarv, expected baʔarˈu
E       assert 'vaʔˈarv' == 'baʔarˈu'
E         
E         - baʔarˈu
E         + vaʔˈarv

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e2\u05b4\u05e8\u05b0\u05e2\u05b2\u05e8\u05d5\u05bc-\u0294ir\u0294ar\u02c8u] _

word = 'עִרְעֲרוּ', expected = 'ʔirʔarˈu'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עִרְעֲרוּ: got ʔirʔˈarv, expected ʔirʔarˈu
E       assert 'ʔirʔˈarv' == 'ʔirʔarˈu'
E         
E         - ʔirʔarˈu
E         ?       ^^
E         + ʔirʔˈarv
E         ?     +  ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d7\u05b2\u05ea\u05bb\u05d5\u05e0\u05bc\u05b8\u05d4-xatun\u02c8a] _

word = 'חֲתֻונָּה', expected = 'xatunˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: חֲתֻונָּה: got xatuunˈa, expected xatunˈa
E       assert 'xatuunˈa' == 'xatunˈa'
E         
E         - xatunˈa
E         + xatuunˈa
E         ?     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d7\u05b3\u05d3\u05b8\u05e9\u05c1\u05b4\u05ab\u05d9\u05dd-xoda\u0283\u02c8im0] _

word = 'חֳדָשִׁ֫ים', expected = 'xodaʃˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: חֳדָשִׁ֫ים: got xodaʃˈijm, expected xodaʃˈim
E       assert 'xodaʃˈijm' == 'xodaʃˈim'
E         
E         - xodaʃˈim
E         + xodaʃˈijm
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e1\u05b0\u05e4\u05d5\u05bc\u05e8\u05b4\u05ab\u05d9\u05dd-sfur\u02c8im] _

word = 'סְפוּרִ֫ים', expected = 'sfurˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סְפוּרִ֫ים: got sfurˈijm, expected sfurˈim
E       assert 'sfurˈijm' == 'sfurˈim'
E         
E         - sfurˈim
E         + sfurˈijm
E         ?       +

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05db\u05bc\u05b8\u05ab\u05da\u05b0-k\u02c8ax0] ________

word = 'כָּ֫ךְ', expected = 'kˈax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כָּ֫ךְ: got xˈax, expected kˈax
E       assert 'xˈax' == 'kˈax'
E         
E         - kˈax
E         ? ^
E         + xˈax
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d0\u05b4\u05e9\u05bc\u05c1\u05ab\u05d5\u05bc\u05dd-be\u0294i\u0283\u02c8um] _

word = 'בְּֽאִשּׁ֫וּם', expected = 'beʔiʃˈum'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בְּֽאִשּׁ֫וּם: got veʔiʃˈum, expected beʔiʃˈum
E       assert 'veʔiʃˈum' == 'beʔiʃˈum'
E         
E         - beʔiʃˈum
E         ? ^
E         + veʔiʃˈum
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b7\u05db\u05bc\u05b6\u05ab\u05e1\u05b6\u05e3-hak\u02c8esef] _

word = 'הַכֶּ֫סֶף', expected = 'hakˈesef'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הַכֶּ֫סֶף: got haxˈesef, expected hakˈesef
E       assert 'haxˈesef' == 'hakˈesef'
E         
E         - hakˈesef
E         ?   ^
E         + haxˈesef
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d5\u05b0\u05bd\u05d4\u05b7\u05e1\u05bc\u05b0\u05d8\u05b7\u05ab\u05e8\u05b0\u05d8\u05b0\u05d0\u05b7\u05e4\u05bc-vehast\u02c8art\u0294ap] _

word = 'וְֽהַסְּטַ֫רְטְאַפּ', expected = 'vehastˈartʔap'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: וְֽהַסְּטַ֫רְטְאַפּ: got , expected vehastˈartʔap
E       assert '' == 'vehastˈartʔap'
E         
E         - vehastˈartʔap

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 39 has multiple outgoing arcs
_ test_phonemize[\u05e0\u05b4\u05de\u05b0\u05db\u05bc\u05b7\u05ab\u05e8-nimk\u02c8ar] _

word = 'נִמְכַּ֫ר', expected = 'nimkˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: נִמְכַּ֫ר: got nimxˈar, expected nimkˈar
E       assert 'nimxˈar' == 'nimkˈar'
E         
E         - nimkˈar
E         ?    ^
E         + nimxˈar
E         ?    ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d4\u05b6\u05e4\u05b0\u05e1\u05b5\u05ab\u05d3-behefs\u02c8ed] _

word = 'בְּֽהֶפְסֵ֫ד', expected = 'behefsˈed'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בְּֽהֶפְסֵ֫ד: got vehefsˈed, expected behefsˈed
E       assert 'vehefsˈed' == 'behefsˈed'
E         
E         - behefsˈed
E         ? ^
E         + vehefsˈed
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05bc\u05b4\u05de\u05b0\u05e2\u05b7\u05ab\u05d8-kim\u0294\u02c8at] _

word = 'כִּמְעַ֫ט', expected = 'kimʔˈat'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כִּמְעַ֫ט: got ximʔˈat, expected kimʔˈat
E       assert 'ximʔˈat' == 'kimʔˈat'
E         
E         - kimʔˈat
E         ? ^
E         + ximʔˈat
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05bc\u05b7\u05e1\u05b0\u05e4\u05bc\u05b5\u05ab\u05d9-kasp\u02c8ej] _

word = 'כַּסְפֵּ֫י', expected = 'kaspˈej'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כַּסְפֵּ֫י: got xasfˈej, expected kaspˈej
E       assert 'xasfˈej' == 'kaspˈej'
E         
E         - kaspˈej
E         + xasfˈej

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b7\u05de\u05bc\u05b7\u05e9\u05c1\u05b0\u05e7\u05b4\u05d9\u05e2\u05b4\u05ab\u05d9\u05dd-hama\u0283ki\u0294\u02c8im] _

word = 'הַמַּשְׁקִיעִ֫ים', expected = 'hamaʃkiʔˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הַמַּשְׁקִיעִ֫ים: got hamaʃkiʔˈijm, expected hamaʃkiʔˈim
E       assert 'hamaʃkiʔˈijm' == 'hamaʃkiʔˈim'
E         
E         - hamaʃkiʔˈim
E         + hamaʃkiʔˈijm
E         ?           +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b4\u05e9\u05c1\u05b0\u05ea\u05bc\u05b7\u05de\u05bc\u05b5\u05ab\u05e9\u05c1-hi\u0283tam\u02c8e\u0283] _

word = 'הִשְׁתַּמֵּ֫שׁ', expected = 'hiʃtamˈeʃ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הִשְׁתַּמֵּ֫שׁ: got , expected hiʃtamˈeʃ
E       assert '' == 'hiʃtamˈeʃ'
E         
E         - hiʃtamˈeʃ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 30 has multiple outgoing arcs
_ test_phonemize[\u05d1\u05bc\u05b7\u05de\u05bc\u05b5\u05d0\u05ab\u05d5\u05b9\u05ea-bame\u0294\u02c8ot] _

word = 'בַּמֵּא֫וֹת', expected = 'bameʔˈot'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בַּמֵּא֫וֹת: got vameʔˈot, expected bameʔˈot
E       assert 'vameʔˈot' == 'bameʔˈot'
E         
E         - bameʔˈot
E         ? ^
E         + vameʔˈot
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e7\u05b7\u05d1\u05bc\u05b0\u05dc\u05b8\u05e0\u05b4\u05ab\u05d9\u05dd-kablan\u02c8im] _

word = 'קַבְּלָנִ֫ים', expected = 'kablanˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: קַבְּלָנִ֫ים: got kaulanˈijm, expected kablanˈim
E       assert 'kaulanˈijm' == 'kablanˈim'
E         
E         - kablanˈim
E         ?   ^
E         + kaulanˈijm
E         ?   ^     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e8\u05b0\u05bd\u05db\u05b4\u05d9\u05e9\u05c1\u05b8\u05ab\u05d4-rexi\u0283\u02c8a] _

word = 'רְֽכִישָׁ֫ה', expected = 'rexiʃˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רְֽכִישָׁ֫ה: got rexiʃˈah, expected rexiʃˈa
E       assert 'rexiʃˈah' == 'rexiʃˈa'
E         
E         - rexiʃˈa
E         + rexiʃˈah
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d1\u05b4\u05e0\u05b0\u05d9\u05b7\u05ab\u05df-bevinj\u02c8an] _

word = 'בְּֽבִנְיַ֫ן', expected = 'bevinjˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בְּֽבִנְיַ֫ן: got vevinjˈan, expected bevinjˈan
E       assert 'vevinjˈan' == 'bevinjˈan'
E         
E         - bevinjˈan
E         ? ^
E         + vevinjˈan
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b4\u05e9\u05c2\u05b0\u05e8\u05b8\u05d3\u05b4\u05ab\u05d9\u05dd-misrad\u02c8im] _

word = 'מִשְׂרָדִ֫ים', expected = 'misradˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מִשְׂרָדִ֫ים: got miʃradˈijm, expected misradˈim
E       assert 'miʃradˈijm' == 'misradˈim'
E         
E         - misradˈim
E         ?   ^
E         + miʃradˈijm
E         ?   ^     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05e4\u05b4\u05d9\u05dc\u05b4\u05d9\u05e4\u05bc\u05b4\u05ab\u05d9\u05e0\u05b4\u05d9\u05dd-befilip\u02c8inim] _

word = 'בְּֽפִילִיפִּ֫ינִים', expected = 'befilipˈinim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בְּֽפִילִיפִּ֫ינִים: got vefilifˈijnim, expected befilipˈinim
E       assert 'vefilifˈijnim' == 'befilipˈinim'
E         
E         - befilipˈinim
E         ? ^     ^
E         + vefilifˈijnim
E         ? ^     ^  +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05bc\u05b0\u05bd\u05d3\u05b5\u05ab\u05d9-ked\u02c8ej] _

word = 'כְּֽדֵ֫י', expected = 'kedˈej'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כְּֽדֵ֫י: got xedˈej, expected kedˈej
E       assert 'xedˈej' == 'kedˈej'
E         
E         - kedˈej
E         ? ^
E         + xedˈej
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b0\u05bd\u05d4\u05b7\u05e9\u05c1\u05b0\u05dc\u05b4\u05ab\u05d9\u05dd-leha\u0283l\u02c8im] _

word = 'לְֽהַשְׁלִ֫ים', expected = 'lehaʃlˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לְֽהַשְׁלִ֫ים: got lehaʃlˈijm, expected lehaʃlˈim
E       assert 'lehaʃlˈijm' == 'lehaʃlˈim'
E         
E         - lehaʃlˈim
E         + lehaʃlˈijm
E         ?         +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d9\u05b0\u05d3\u05b8\u05e0\u05b4\u05ab\u05d9\u05ea-jdan\u02c8it] _

word = 'יְדָנִ֫ית', expected = 'jdanˈit'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: יְדָנִ֫ית: got jdanˈijt, expected jdanˈit
E       assert 'jdanˈijt' == 'jdanˈit'
E         
E         - jdanˈit
E         + jdanˈijt
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e9\u05c1\u05b6\u05d1\u05bc\u05bb\u05e6\u05bc\u05b0\u05e2\u05ab\u05d5\u05bc-\u0283ebuts\u0294\u02c8u] _

word = 'שֶׁבֻּצְּע֫וּ', expected = 'ʃebutsʔˈu'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שֶׁבֻּצְּע֫וּ: got ʃevutsʔˈv, expected ʃebutsʔˈu
E       assert 'ʃevutsʔˈv' == 'ʃebutsʔˈu'
E         
E         - ʃebutsʔˈu
E         ?   ^     ^
E         + ʃevutsʔˈv
E         ?   ^     ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b8\u05d0\u05b7\u05e4\u05bc\u05b0\u05dc\u05b4\u05d9\u05e7\u05b7\u05ab\u05e6\u05b0\u05d9\u05b8\u05d4-ha\u0294aplik\u02c8atsja] _

word = 'הָאַפְּלִיקַ֫צְיָה', expected = 'haʔaplikˈatsja'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הָאַפְּלִיקַ֫צְיָה: got haʔaflikˈatsja, expected haʔaplikˈatsja
E       assert 'haʔaflikˈatsja' == 'haʔaplikˈatsja'
E         
E         - haʔaplikˈatsja
E         ?     ^
E         + haʔaflikˈatsja
E         ?     ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b7\u05d4\u05d5\u05b9\u05d3\u05b8\u05e2\u05b8\u05ab\u05d4-bahoda\u0294\u02c8a] _

word = 'בַּהוֹדָעָ֫ה', expected = 'bahodaʔˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בַּהוֹדָעָ֫ה: got vahodaʔˈah, expected bahodaʔˈa
E       assert 'vahodaʔˈah' == 'bahodaʔˈa'
E         
E         - bahodaʔˈa
E         ? ^
E         + vahodaʔˈah
E         ? ^        +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05db\u05bc\u05b0\u05ea\u05b7\u05ab\u05d1-kt\u02c8av] _____

word = 'כְּתַ֫ב', expected = 'ktˈav'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כְּתַ֫ב: got xtˈav, expected ktˈav
E       assert 'xtˈav' == 'ktˈav'
E         
E         - ktˈav
E         ? ^
E         + xtˈav
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b4\u05e9\u05c2\u05b0\u05e8\u05b7\u05ab\u05d3-misr\u02c8ad] _

word = 'מִשְׂרַ֫ד', expected = 'misrˈad'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מִשְׂרַ֫ד: got miʃrˈad, expected misrˈad
E       assert 'miʃrˈad' == 'misrˈad'
E         
E         - misrˈad
E         ?   ^
E         + miʃrˈad
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b7\u05de\u05bc\u05b4\u05e9\u05c1\u05b0\u05e4\u05bc\u05b8\u05d8\u05b4\u05ab\u05d9\u05dd-hami\u0283pat\u02c8im] _

word = 'הַמִּשְׁפָּטִ֫ים', expected = 'hamiʃpatˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הַמִּשְׁפָּטִ֫ים: got hamiʃfatˈijm, expected hamiʃpatˈim
E       assert 'hamiʃfatˈijm' == 'hamiʃpatˈim'
E         
E         - hamiʃpatˈim
E         ?      ^
E         + hamiʃfatˈijm
E         ?      ^    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d0\u05b5\u05d6\u05ab\u05d5\u05b9\u05e8-be\u0294ez\u02c8or] _

word = 'בְּֽאֵז֫וֹר', expected = 'beʔezˈor'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בְּֽאֵז֫וֹר: got veʔezˈor, expected beʔezˈor
E       assert 'veʔezˈor' == 'beʔezˈor'
E         
E         - beʔezˈor
E         ? ^
E         + veʔezˈor
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b7\u05d7\u05b7\u05d2\u05bc\u05b4\u05ab\u05d9\u05dd-haxag\u02c8im] _

word = 'הַחַגִּ֫ים', expected = 'haxagˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הַחַגִּ֫ים: got haxagˈijm, expected haxagˈim
E       assert 'haxagˈijm' == 'haxagˈim'
E         
E         - haxagˈim
E         + haxagˈijm
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b8\u05e2\u05b2\u05de\u05d5\u05bc\u05e1\u05b8\u05ab\u05d4-ha\u0294amus\u02c8a] _

word = 'הָעֲמוּסָ֫ה', expected = 'haʔamusˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הָעֲמוּסָ֫ה: got haʔamusˈah, expected haʔamusˈa
E       assert 'haʔamusˈah' == 'haʔamusˈa'
E         
E         - haʔamusˈa
E         + haʔamusˈah
E         ?          +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b4\u05e1\u05b0\u05e4\u05bc\u05b7\u05ab\u05e8-misp\u02c8ar] _

word = 'מִסְפַּ֫ר', expected = 'mispˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מִסְפַּ֫ר: got misfˈar, expected mispˈar
E       assert 'misfˈar' == 'mispˈar'
E         
E         - mispˈar
E         ?    ^
E         + misfˈar
E         ?    ^

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05db\u05bc\u05b8\u05ab\u05da\u05b0-k\u02c8ax1] ________

word = 'כָּ֫ךְ', expected = 'kˈax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כָּ֫ךְ: got xˈax, expected kˈax
E       assert 'xˈax' == 'kˈax'
E         
E         - kˈax
E         ? ^
E         + xˈax
E         ? ^

tests/test_phonemize.py:16: AssertionError
______________ test_phonemize[\u05dc\u05b9\u05ab\u05d0-l\u02c8o] _______________

word = 'לֹ֫א', expected = 'lˈo'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לֹ֫א: got lˈoʔ, expected lˈo
E       assert 'lˈoʔ' == 'lˈo'
E         
E         - lˈo
E         + lˈoʔ
E         ?    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b4\u05e9\u05c1\u05b0\u05ea\u05bc\u05b7\u05de\u05bc\u05b5\u05ab\u05e9\u05c1-mi\u0283tam\u02c8e\u0283] _

word = 'מִשְׁתַּמֵּ֫שׁ', expected = 'miʃtamˈeʃ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מִשְׁתַּמֵּ֫שׁ: got , expected miʃtamˈeʃ
E       assert '' == 'miʃtamˈeʃ'
E         
E         - miʃtamˈeʃ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 30 has multiple outgoing arcs
_ test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d1\u05ab\u05d5\u05b9\u05d8\u05b4\u05d9\u05dd-bev\u02c8otim] _

word = 'בְּֽב֫וֹטִים', expected = 'bevˈotim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בְּֽב֫וֹטִים: got vevˈotim, expected bevˈotim
E       assert 'vevˈotim' == 'bevˈotim'
E         
E         - bevˈotim
E         ? ^
E         + vevˈotim
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d1\u05bc\u05ab\u05d5\u05b9\u05d8\u05b4\u05d9\u05dd-b\u02c8otim] _

word = 'בּ֫וֹטִים', expected = 'bˈotim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בּ֫וֹטִים: got , expected bˈotim
E       assert '' == 'bˈotim'
E         
E         - bˈotim

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 3 has multiple outgoing arcs
_ test_phonemize[\u05d8\u05b4\u05e4\u05bc\u05b0\u05e9\u05c1\u05b4\u05ab\u05d9\u05dd-tip\u0283\u02c8im] _

word = 'טִפְּשִׁ֫ים', expected = 'tipʃˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: טִפְּשִׁ֫ים: got tifʃˈijm, expected tipʃˈim
E       assert 'tifʃˈijm' == 'tipʃˈim'
E         
E         - tipʃˈim
E         ?   ^
E         + tifʃˈijm
E         ?   ^   +

tests/test_phonemize.py:16: AssertionError
_____ test_phonemize[\u05db\u05bc\u05b0\u05e4\u05b4\u05ab\u05d9-kf\u02c8i] _____

word = 'כְּפִ֫י', expected = 'kfˈi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כְּפִ֫י: got xfˈij, expected kfˈi
E       assert 'xfˈij' == 'kfˈi'
E         
E         - kfˈi
E         + xfˈij

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e7\u05b8\u05e8\u05b8\u05ab\u05d0-kar\u02c8a] ________

word = 'קָרָ֫א', expected = 'karˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: קָרָ֫א: got karˈaʔ, expected karˈa
E       assert 'karˈaʔ' == 'karˈa'
E         
E         - karˈa
E         + karˈaʔ
E         ?      +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e9\u05c1\u05d5\u05bc\u05dc\u05b7\u05de\u05bc\u05b4\u05ab\u05d9\u05ea-\u0283ulam\u02c8it] _

word = 'שׁוּלַמִּ֫ית', expected = 'ʃulamˈit'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שׁוּלַמִּ֫ית: got , expected ʃulamˈit
E       assert '' == 'ʃulamˈit'
E         
E         - ʃulamˈit

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 3 has multiple outgoing arcs
_ test_phonemize[\u05d9\u05b7\u05d3\u05b8\u05e0\u05b4\u05ab\u05d9\u05ea-jadan\u02c8it] _

word = 'יַדָנִ֫ית', expected = 'jadanˈit'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: יַדָנִ֫ית: got jadanˈijt, expected jadanˈit
E       assert 'jadanˈijt' == 'jadanˈit'
E         
E         - jadanˈit
E         + jadanˈijt
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e1\u05b4\u05e8\u05b0\u05d8\u05d5\u05b9\u05e0\u05b4\u05ab\u05d9\u05dd-sirton\u02c8im] _

word = 'סִרְטוֹנִ֫ים', expected = 'sirtonˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סִרְטוֹנִ֫ים: got sirtonˈijm, expected sirtonˈim
E       assert 'sirtonˈijm' == 'sirtonˈim'
E         
E         - sirtonˈim
E         + sirtonˈijm
E         ?         +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e6\u05d5\u05b9\u05e4\u05b4\u05ab\u05d9\u05dd-tsof\u02c8im] _

word = 'צוֹפִ֫ים', expected = 'tsofˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צוֹפִ֫ים: got tsofˈijm, expected tsofˈim
E       assert 'tsofˈijm' == 'tsofˈim'
E         
E         - tsofˈim
E         + tsofˈijm
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d2\u05bc\u05b0\u05d3\u05b4\u05d9\u05dc\u05b8\u05ab\u05d4-gdil\u02c8a] _

word = 'גְּדִילָ֫ה', expected = 'gdilˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: גְּדִילָ֫ה: got gdilˈah, expected gdilˈa
E       assert 'gdilˈah' == 'gdilˈa'
E         
E         - gdilˈa
E         + gdilˈah
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e4\u05bc\u05b4\u05ea\u05bc\u05ab\u05d5\u05bc\u05d7\u05b7-pit\u02c8uax] _

word = 'פִּתּ֫וּחַ', expected = 'pitˈuax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: פִּתּ֫וּחַ: got fitˈuax, expected pitˈuax
E       assert 'fitˈuax' == 'pitˈuax'
E         
E         - pitˈuax
E         ? ^
E         + fitˈuax
E         ? ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b4\u05d2\u05bc'\u05d5\u05b9\u05e0\u05b0\u05e8\u05b8\u05d8\u05b4\u05ab\u05d9\u05dd-mid\u0292onrat\u02c8im] _

word = "מִגּ'וֹנְרָטִ֫ים", expected = 'midʒonratˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מִגּ'וֹנְרָטִ֫ים: got , expected midʒonratˈim
E       assert '' == 'midʒonratˈim'
E         
E         - midʒonratˈim

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
____ test_phonemize[\u05d6\u05b8'\u05e7\u05b5\u05ab\u05d8-\u0292ak\u02c8et] ____

word = "זָ'קֵ֫ט", expected = 'ʒakˈet'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: זָ'קֵ֫ט: got , expected ʒakˈet
E       assert '' == 'ʒakˈet'
E         
E         - ʒakˈet

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d7\u05b3\u05d3\u05b8\u05e9\u05c1\u05b4\u05ab\u05d9\u05dd-xoda\u0283\u02c8im1] _

word = 'חֳדָשִׁ֫ים', expected = 'xodaʃˈim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: חֳדָשִׁ֫ים: got xodaʃˈijm, expected xodaʃˈim
E       assert 'xodaʃˈijm' == 'xodaʃˈim'
E         
E         - xodaʃˈim
E         + xodaʃˈijm
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e2\u05b2\u05d1\u05d5\u05b9\u05d3\u05b8\u05ab\u05d4-\u0294avod\u02c8a] _

word = 'עֲבוֹדָ֫ה', expected = 'ʔavodˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עֲבוֹדָ֫ה: got ʔavodˈah, expected ʔavodˈa
E       assert 'ʔavodˈah' == 'ʔavodˈa'
E         
E         - ʔavodˈa
E         + ʔavodˈah
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b7\u05e1\u05b0\u05e4\u05bc\u05b4\u05ab\u05d9\u05e7-masp\u02c8ik] _

word = 'מַסְפִּ֫יק', expected = 'maspˈik'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מַסְפִּ֫יק: got masfˈijk, expected maspˈik
E       assert 'masfˈijk' == 'maspˈik'
E         
E         - maspˈik
E         ?    ^
E         + masfˈijk
E         ?    ^  +

tests/test_phonemize.py:16: AssertionError
__ test_phonemize[\u05d0\u05b5\u05ab\u05dc\u05bc\u05d5\u05bc-\u0294\u02c8elu] __

word = 'אֵ֫לּוּ', expected = 'ʔˈelu'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֵ֫לּוּ: got ʔˈelv, expected ʔˈelu
E       assert 'ʔˈelv' == 'ʔˈelu'
E         
E         - ʔˈelu
E         ?     ^
E         + ʔˈelv
E         ?     ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b0\u05bd\u05d4\u05b4\u05db\u05bc\u05b8\u05e9\u05c1\u05b5\u05ab\u05dc-lehika\u0283\u02c8el] _

word = 'לְֽהִכָּשֵׁ֫ל', expected = 'lehikaʃˈel'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לְֽהִכָּשֵׁ֫ל: got lehixaʃˈel, expected lehikaʃˈel
E       assert 'lehixaʃˈel' == 'lehikaʃˈel'
E         
E         - lehikaʃˈel
E         ?     ^
E         + lehixaʃˈel
E         ?     ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05ea\u05bc\u05b7\u05e4\u05b0\u05e7\u05b4\u05ab\u05d9\u05d3-tafk\u02c8id] _

word = 'תַּפְקִ֫יד', expected = 'tafkˈid'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: תַּפְקִ֫יד: got tafkˈijd, expected tafkˈid
E       assert 'tafkˈijd' == 'tafkˈid'
E         
E         - tafkˈid
E         + tafkˈijd
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b0\u05bd\u05e9\u05c2\u05b4\u05d9\u05de\u05b8\u05ab\u05d4-mesim\u02c8a] _

word = 'מְֽשִׂימָ֫ה', expected = 'mesimˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽשִׂימָ֫ה: got meʃimˈah, expected mesimˈa
E       assert 'meʃimˈah' == 'mesimˈa'
E         
E         - mesimˈa
E         ?   ^
E         + meʃimˈah
E         ?   ^    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b0\u05bd\u05e6\u05bb\u05e4\u05bc\u05b6\u05ab\u05d4-metsup\u02c8e] _

word = 'מְֽצֻפֶּ֫ה', expected = 'metsupˈe'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽצֻפֶּ֫ה: got metsufˈeh, expected metsupˈe
E       assert 'metsufˈeh' == 'metsupˈe'
E         
E         - metsupˈe
E         ?      ^
E         + metsufˈeh
E         ?      ^  +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d2\u05bc\u05ab'\u05d5\u05bc\u05e0\u05b0\u05d9\u05d5\u05b9\u05e8-d\u0292\u02c8unjor] _

word = "גּ֫'וּנְיוֹר", expected = 'dʒˈunjor'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: גּ֫'וּנְיוֹר: got , expected dʒˈunjor
E       assert '' == 'dʒˈunjor'
E         
E         - dʒˈunjor

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d0\u05b4\u05d9\u05b8\u05bc\u05ab\u05e8-\u0294ij\u02c8ar0] _

word = 'אִיָּ֫ר', expected = 'ʔijˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אִיָּ֫ר: got ʔˈiar, expected ʔijˈar
E       assert 'ʔˈiar' == 'ʔijˈar'
E         
E         - ʔijˈar
E         + ʔˈiar

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05e9\u05b7\u05c2\u05de\u05b0\u05ea\u05b8\u05bc-samta] ____

word = 'שַׂמְתָּ', expected = 'samta'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שַׂמְתָּ: got ʃamtˈa, expected samta
E       assert 'ʃamtˈa' == 'samta'
E         
E         - samta
E         + ʃamtˈa

tests/test_phonemize.py:16: AssertionError
______ test_phonemize[\u05e6\u05b7\u05d4\u05b7\u05f4\u05dc-ts\u02c8ahal] _______

word = 'צַהַ״ל', expected = 'tsˈahal'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צַהַ״ל: got , expected tsˈahal
E       assert '' == 'tsˈahal'
E         
E         - tsˈahal

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
________ test_phonemize[\u05e6\u05b7\u05d4\u05b7"\u05dc-ts\u02c8ahal0] _________

word = 'צַהַ"ל', expected = 'tsˈahal'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צַהַ"ל: got , expected tsˈahal
E       assert '' == 'tsˈahal'
E         
E         - tsˈahal

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05db\u05b7\u05bc\u05d4\u05b2\u05dc\u05b8\u05db\u05b8\u05d4-kahalax\u02c8a0] _

word = 'כַּהֲלָכָה', expected = 'kahalaxˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כַּהֲלָכָה: got xahalaˈax, expected kahalaxˈa
E       assert 'xahalaˈax' == 'kahalaxˈa'
E         
E         - kahalaxˈa
E         ? ^     -
E         + xahalaˈax
E         ? ^       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05ea\u05b8\u05bc\u05de\u05d5\u05bc\u05d4\u05b7\u05bc-tamu\u02c8a] _

word = 'תָּמוּהַּ', expected = 'tamuˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: תָּמוּהַּ: got tamuhˈa, expected tamuˈa
E       assert 'tamuhˈa' == 'tamuˈa'
E         
E         - tamuˈa
E         + tamuhˈa
E         ?     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d2\u05b8\u05bc\u05d1\u05d5\u05b9\u05d4\u05b7\u05bc-gavo\u02c8a] _

word = 'גָּבוֹהַּ', expected = 'gavoˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: גָּבוֹהַּ: got gavohˈa, expected gavoˈa
E       assert 'gavohˈa' == 'gavoˈa'
E         
E         - gavoˈa
E         + gavohˈa
E         ?     +

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e9\u05c2\u05b4\u05d9\u05d7\u05b7-si\u02c8ax] ________

word = 'שִׂיחַ', expected = 'siˈax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שִׂיחַ: got ʃiˈax, expected siˈax
E       assert 'ʃiˈax' == 'siˈax'
E         
E         - siˈax
E         ? ^
E         + ʃiˈax
E         ? ^

tests/test_phonemize.py:16: AssertionError
___________ test_phonemize[\u05dc\u05b9\u05ab\u05e2\u05b7-l\u02c8oa] ___________

word = 'לֹ֫עַ', expected = 'lˈoa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לֹ֫עַ: got lˈoʔa, expected lˈoa
E       assert 'lˈoʔa' == 'lˈoa'
E         
E         - lˈoa
E         + lˈoʔa
E         ?    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b4\u05e9\u05b0\u05c1\u05e7\u05b9\u05e2\u05b7-li\u0283koa] _

word = 'לִשְׁקֹעַ', expected = 'liʃkoa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִשְׁקֹעַ: got liʃkoʔˈa, expected liʃkoa
E       assert 'liʃkoʔˈa' == 'liʃkoa'
E         
E         - liʃkoa
E         + liʃkoʔˈa
E         ?      ++

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e7\u05b8\u05dc\u05b4\u05d9\u05e2\u05b7-kalia] _______

word = 'קָלִיעַ', expected = 'kalia'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: קָלִיעַ: got kaliʔˈa, expected kalia
E       assert 'kaliʔˈa' == 'kalia'
E         
E         - kalia
E         + kaliʔˈa
E         ?     ++

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05e4\u05b8\u05bc\u05e8\u05d5\u05bc\u05e2\u05b7-parua] ____

word = 'פָּרוּעַ', expected = 'parua'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: פָּרוּעַ: got faruʔˈa, expected parua
E       assert 'faruʔˈa' == 'parua'
E         
E         - parua
E         + faruʔˈa

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05e7\u05b8\u05dc\u05b0\u05e2\u05b8\u05d4-kal\u0294a] _____

word = 'קָלְעָה', expected = 'kalʔa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: קָלְעָה: got kalʔˈa, expected kalʔa
E       assert 'kalʔˈa' == 'kalʔa'
E         
E         - kalʔa
E         + kalʔˈa
E         ?     +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05e7\u05b8\u05e8\u05b0\u05d0\u05b8\u05d4-kar\u0294a] _____

word = 'קָרְאָה', expected = 'karʔa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: קָרְאָה: got karʔˈa, expected karʔa
E       assert 'karʔˈa' == 'karʔa'
E         
E         - karʔa
E         + karʔˈa
E         ?     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b0\u05bd\u05d2\u05bb\u05d5\u05b8\u05bc\u05df-meguvan0] _

word = 'מְֽגֻוָּן', expected = 'meguvan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽגֻוָּן: got meguvˈan, expected meguvan
E       assert 'meguvˈan' == 'meguvan'
E         
E         - meguvan
E         + meguvˈan
E         ?      +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05e2\u05b4\u05d5\u05bc\u05d5\u05bc\u05ea-\u0294ivut0] ____

word = 'עִוּוּת', expected = 'ʔivut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עִוּוּת: got ʔivˈut, expected ʔivut
E       assert 'ʔivˈut' == 'ʔivut'
E         
E         - ʔivut
E         + ʔivˈut
E         ?    +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05d0\u05b4\u05d9\u05bc\u05d5\u05bc\u05ea-\u0294ijut0] ____

word = 'אִיּוּת', expected = 'ʔijut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אִיּוּת: got ʔiˈut, expected ʔijut
E       assert 'ʔiˈut' == 'ʔijut'
E         
E         - ʔijut
E         ?   ^
E         + ʔiˈut
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d5\u05b0\u05d4\u05b4\u05ea\u05b0\u05d7\u05b4\u05d9\u05dc-vehitxil] _

word = 'וְהִתְחִיל', expected = 'vehitxil'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: וְהִתְחִיל: got uhitxˈil, expected vehitxil
E       assert 'uhitxˈil' == 'vehitxil'
E         
E         - vehitxil
E         ? ^^
E         + uhitxˈil
E         ? ^    +

tests/test_phonemize.py:16: AssertionError
___ test_phonemize[\u05d4\u05b2\u05d2\u05b7\u05e0\u05b8\u05bc\u05d4-hagana] ____

word = 'הֲגַנָּה', expected = 'hagana'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הֲגַנָּה: got haganˈa, expected hagana
E       assert 'haganˈa' == 'hagana'
E         
E         - hagana
E         + haganˈa
E         ?      +

tests/test_phonemize.py:16: AssertionError
__________ test_phonemize[\u05d8\u05b7\u05d5\u05bc\u05b8\u05e1-tavas] __________

word = 'טַוָּס', expected = 'tavas'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: טַוָּס: got tavˈas, expected tavas
E       assert 'tavˈas' == 'tavas'
E         
E         - tavas
E         + tavˈas
E         ?    +

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e2\u05b4\u05d5\u05bc\u05b5\u05e8-\u0294iver] ________

word = 'עִוֵּר', expected = 'ʔiver'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עִוֵּר: got ʔivˈer, expected ʔiver
E       assert 'ʔivˈer' == 'ʔiver'
E         
E         - ʔiver
E         + ʔivˈer
E         ?    +

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e2\u05b8\u05d5\u05d5\u05b9\u05df-\u0294avon] ________

word = 'עָווֹן', expected = 'ʔavon'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עָווֹן: got ʔavˈon, expected ʔavon
E       assert 'ʔavˈon' == 'ʔavon'
E         
E         - ʔavon
E         + ʔavˈon
E         ?    +

tests/test_phonemize.py:16: AssertionError
___ test_phonemize[\u05dc\u05b4\u05d2\u05b0\u05d5\u05b9\u05e2\u05b7-ligvoa] ____

word = 'לִגְוֹעַ', expected = 'ligvoa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִגְוֹעַ: got ligoʔˈa, expected ligvoa
E       assert 'ligoʔˈa' == 'ligvoa'
E         
E         - ligvoa
E         ?    -
E         + ligoʔˈa
E         ?     ++

tests/test_phonemize.py:16: AssertionError
__________ test_phonemize[\u05d5\u05d5\u05b9\u05dc\u05b0\u05d8-volt] ___________

word = 'ווֹלְט', expected = 'volt'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: ווֹלְט: got vˈolt, expected volt
E       assert 'vˈolt' == 'volt'
E         
E         - volt
E         + vˈolt
E         ?  +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b0\u05bd\u05d2\u05bb\u05d5\u05b8\u05bc\u05df-meguvan1] _

word = 'מְֽגֻוָּן', expected = 'meguvan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽגֻוָּן: got meguvˈan, expected meguvan
E       assert 'meguvˈan' == 'meguvan'
E         
E         - meguvan
E         + meguvˈan
E         ?      +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05e2\u05b4\u05d5\u05bc\u05d5\u05bc\u05ea-\u0294ivut1] ____

word = 'עִוּוּת', expected = 'ʔivut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עִוּוּת: got ʔivˈut, expected ʔivut
E       assert 'ʔivˈut' == 'ʔivut'
E         
E         - ʔivut
E         + ʔivˈut
E         ?    +

tests/test_phonemize.py:16: AssertionError
____ test_phonemize[\u05d0\u05b4\u05d9\u05bc\u05d5\u05bc\u05ea-\u0294ijut1] ____

word = 'אִיּוּת', expected = 'ʔijut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אִיּוּת: got ʔiˈut, expected ʔijut
E       assert 'ʔiˈut' == 'ʔijut'
E         
E         - ʔijut
E         ?   ^
E         + ʔiˈut
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b4\u05d5\u05b0\u05d9\u05b8\u05ea\u05b8\u05ab\u05df-livjat\u02c8an] _

word = 'לִוְיָתָ֫ן', expected = 'livjatˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִוְיָתָ֫ן: got liujatˈan, expected livjatˈan
E       assert 'liujatˈan' == 'livjatˈan'
E         
E         - livjatˈan
E         ?   ^
E         + liujatˈan
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e2\u05b7\u05db\u05b0\u05e9\u05c1\u05b8\u05ab\u05d9\u05d5-\u0294ax\u0283\u02c8av] _

word = 'עַכְשָׁ֫יו', expected = 'ʔaxʃˈav'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עַכְשָׁ֫יו: got ʔaxʃˈajv, expected ʔaxʃˈav
E       assert 'ʔaxʃˈajv' == 'ʔaxʃˈav'
E         
E         - ʔaxʃˈav
E         + ʔaxʃˈajv
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e8\u05ab\u05d5\u05b9\u05dc\u05b6\u05e8\u05b0\u05d1\u05b0\u05bc\u05dc\u05b6\u05d9\u05b0\u05d3\u05b0\u05e1-r\u02c8olerblejds] _

word = 'ר֫וֹלֶרְבְּלֶיְדְס', expected = 'rˈolerblejds'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: ר֫וֹלֶרְבְּלֶיְדְס: got rˈolerulejds, expected rˈolerblejds
E       assert 'rˈolerulejds' == 'rˈolerblejds'
E         
E         - rˈolerblejds
E         ?       ^
E         + rˈolerulejds
E         ?       ^

tests/test_phonemize.py:16: AssertionError
______ test_phonemize[\u05e8\u05b8\u05ab\u05de\u05b8"\u05d7-r\u02c8amax] _______

word = 'רָ֫מָ"ח', expected = 'rˈamax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רָ֫מָ"ח: got , expected rˈamax
E       assert '' == 'rˈamax'
E         
E         - rˈamax

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
________ test_phonemize[\u05e6\u05b7\u05d4\u05b7"\u05dc-ts\u02c8ahal1] _________

word = 'צַהַ"ל', expected = 'tsˈahal'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צַהַ"ל: got , expected tsˈahal
E       assert '' == 'tsˈahal'
E         
E         - tsˈahal

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d9\u05b4\u05e9\u05b8\u05bc\u05c2\u05e9\u05db\u05b8\u05ab\u05e8-jisax\u02c8ar] _

word = 'יִשָּׂשכָ֫ר', expected = 'jisaxˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: יִשָּׂשכָ֫ר: got jiʃaʃxˈar, expected jisaxˈar
E       assert 'jiʃaʃxˈar' == 'jisaxˈar'
E         
E         - jisaxˈar
E         ?   ^
E         + jiʃaʃxˈar
E         ?   ^ +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d5\u05b7\u05e1\u05b7\u05d1\u05b4\u05bc\u05d9-was\u02c8abi] _

word = 'וַסַבִּי', expected = 'wasˈabi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: וַסַבִּי: got vasavˈi, expected wasˈabi
E       assert 'vasavˈi' == 'wasˈabi'
E         
E         - wasˈabi
E         + vasavˈi

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05b7\u05bc\u05d4\u05b2\u05dc\u05b8\u05db\u05b8\u05d4-kahalax\u02c8a1] _

word = 'כַּהֲלָכָה', expected = 'kahalaxˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כַּהֲלָכָה: got xahalaˈax, expected kahalaxˈa
E       assert 'xahalaˈax' == 'kahalaxˈa'
E         
E         - kahalaxˈa
E         ? ^     -
E         + xahalaˈax
E         ? ^       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d0\u05b8\u05d6\u05b6\u05e8\u05b0\u05d1\u05b7\u05bc\u05d9\u05b0\u05d2\u05b8'\u05df-\u0294azerbajd\u0292\u02c8an] _

word = "אָזֶרְבַּיְגָ'ן", expected = 'ʔazerbajdʒˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אָזֶרְבַּיְגָ'ן: got , expected ʔazerbajdʒˈan
E       assert '' == 'ʔazerbajdʒˈan'
E         
E         - ʔazerbajdʒˈan

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d0\u05b5\u05ab\u05e8\u05d5\u05b9\u05d2\u05b6'\u05dc-\u0294\u02c8erod\u0292el] _

word = "אֵ֫רוֹגֶ'ל", expected = 'ʔˈerodʒel'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֵ֫רוֹגֶ'ל: got , expected ʔˈerodʒel
E       assert '' == 'ʔˈerodʒel'
E         
E         - ʔˈerodʒel

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_______ test_phonemize[\u05d2'\u05d5\u05b9\u05d1\u05bc-d\u0292\u02c8ob] ________

word = "ג'וֹבּ", expected = 'dʒˈob'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: ג'וֹבּ: got , expected dʒˈob
E       assert '' == 'dʒˈob'
E         
E         - dʒˈob

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d0\u05b8\u05d2\u05b6\u05ab'\u05e0\u05b0\u05d3\u05b8\u05d4-\u0294ad\u0292\u02c8enda] _

word = "אָגֶ֫'נְדָה", expected = 'ʔadʒˈenda'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אָגֶ֫'נְדָה: got , expected ʔadʒˈenda
E       assert '' == 'ʔadʒˈenda'
E         
E         - ʔadʒˈenda

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e4\u05b4\u05bc\u05d9\u05d2\u05b8\u05ab'\u05de\u05b8\u05d4-pid\u0292\u02c8ama] _

word = "פִּיגָ֫'מָה", expected = 'pidʒˈama'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: פִּיגָ֫'מָה: got , expected pidʒˈama
E       assert '' == 'pidʒˈama'
E         
E         - pidʒˈama

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d8\u05b0\u05e8\u05b7\u05e0\u05b0\u05e1\u05b0\u05d2\u05b6\u05ab'\u05e0\u05b0\u05d3\u05b6\u05bc\u05e8-transd\u0292\u02c8ender] _

word = "טְרַנְסְגֶ֫'נְדֶּר", expected = 'transdʒˈender'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: טְרַנְסְגֶ֫'נְדֶּר: got , expected transdʒˈender
E       assert '' == 'transdʒˈender'
E         
E         - transdʒˈender

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e6\u05b4'\u05d9\u05e4\u05b0\u05bc\u05e1-t\u0283\u02c8ips] _

word = "צִ'יפְּס", expected = 'tʃˈips'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צִ'יפְּס: got , expected tʃˈips
E       assert '' == 'tʃˈips'
E         
E         - tʃˈips

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05dc\u05b4\u05ab\u05d9\u05e6\u05b4'\u05d9-l\u02c8it\u0283i] _

word = "לִ֫יצִ'י", expected = 'lˈitʃi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִ֫יצִ'י: got , expected lˈitʃi
E       assert '' == 'lˈitʃi'
E         
E         - lˈitʃi

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05dc\u05b4\u05ab\u05d9\u05e0\u05b0\u05e5'-l\u02c8int\u0283] _

word = "לִ֫ינְץ'", expected = 'lˈintʃ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִ֫ינְץ': got , expected lˈintʃ
E       assert '' == 'lˈintʃ'
E         
E         - lˈintʃ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e6\u05b7\u05ab'\u05e8\u05b0\u05d8\u05b6\u05e8-t\u0283\u02c8arter] _

word = "צַ֫'רְטֶר", expected = 'tʃˈarter'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צַ֫'רְטֶר: got , expected tʃˈarter
E       assert '' == 'tʃˈarter'
E         
E         - tʃˈarter

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
____ test_phonemize[\u05d1\u05b8\u05bc\u05d2\u05b8\u05d6'-bag\u02c8a\u0292] ____

word = "בָּגָז'", expected = 'bagˈaʒ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: בָּגָז': got , expected bagˈaʒ
E       assert '' == 'bagˈaʒ'
E         
E         - bagˈaʒ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d6\u05b7'\u05d1\u05bc\u05d5\u05b9\u05d8\u05b4\u05ab\u05d9\u05e0\u05b0\u05e1\u05b0\u05e7\u05b4\u05d9-\u0292abot\u02c8inski] _

word = "זַ'בּוֹטִ֫ינְסְקִי", expected = 'ʒabotˈinski'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: זַ'בּוֹטִ֫ינְסְקִי: got , expected ʒabotˈinski
E       assert '' == 'ʒabotˈinski'
E         
E         - ʒabotˈinski

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d5\u05b4\u05d9\u05d8\u05b0\u05e8\u05b8\u05d6'-vitr\u02c8a\u0292] _

word = "וִיטְרָז'", expected = 'vitrˈaʒ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: וִיטְרָז': got , expected vitrˈaʒ
E       assert '' == 'vitrˈaʒ'
E         
E         - vitrˈaʒ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
____ test_phonemize[\u05db\u05b0\u05bc\u05e1\u05b4\u05d9\u05dc-ks\u02c8il] _____

word = 'כְּסִיל', expected = 'ksˈil'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כְּסִיל: got xsˈil, expected ksˈil
E       assert 'xsˈil' == 'ksˈil'
E         
E         - ksˈil
E         ? ^
E         + xsˈil
E         ? ^

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05d2\u05b4'\u05d9\u05e4\u05bc-d\u0292\u02c8ip] ________

word = "גִ'יפּ", expected = 'dʒˈip'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: גִ'יפּ: got , expected dʒˈip
E       assert '' == 'dʒˈip'
E         
E         - dʒˈip

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e8\u05c7\u05d7\u05b0\u05d1\u05bc\u05b4\u05d9-roxb\u02c8i] _

word = 'רׇחְבִּי', expected = 'roxbˈi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רׇחְבִּי: got roxvˈi, expected roxbˈi
E       assert 'roxvˈi' == 'roxbˈi'
E         
E         - roxbˈi
E         ?    ^
E         + roxvˈi
E         ?    ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05de\u05b7\u05e6\u05b0\u05dc\u05b4\u05ab\u05d9\u05d7\u05b7-matsl\u02c8iax] _

word = 'מַצְלִ֫יחַ', expected = 'matslˈiax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מַצְלִ֫יחַ: got matslˈijax, expected matslˈiax
E       assert 'matslˈijax' == 'matslˈiax'
E         
E         - matslˈiax
E         + matslˈijax
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d8\u05b0\u05e8\u05b6\u05de\u05b0\u05e4\u05b0\u05bc-tr\u02c8emp] _

word = 'טְרֶמְפְּ', expected = 'trˈemp'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: טְרֶמְפְּ: got trˈemf, expected trˈemp
E       assert 'trˈemf' == 'trˈemp'
E         
E         - trˈemp
E         ?      ^
E         + trˈemf
E         ?      ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05b7\u05bc\u05d1\u05b8\u05bc\u05d1\u05bc-kab\u02c8ab] _

word = 'כַּבָּבּ', expected = 'kabˈab'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כַּבָּבּ: got , expected kabˈab
E       assert '' == 'kabˈab'
E         
E         - kabˈab

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 19 has multiple outgoing arcs
_______ test_phonemize[\u05e1\u05b6\u05dc\u05b6\u05d1\u05bc-sel\u02c8eb] _______

word = 'סֶלֶבּ', expected = 'selˈeb'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סֶלֶבּ: got , expected selˈeb
E       assert '' == 'selˈeb'
E         
E         - selˈeb

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 13 has multiple outgoing arcs
________ test_phonemize[\u05e4\u05b8\u05bc\u05d0\u05d1\u05bc-p\u02c8ab] ________

word = 'פָּאבּ', expected = 'pˈab'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: פָּאבּ: got , expected pˈab
E       assert '' == 'pˈab'
E         
E         - pˈab

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 15 has multiple outgoing arcs
_ test_phonemize[\u05d0\u05c7\u05de\u05bc\u05b8\u05e0\u05d5\u05bc\u05ea-\u0294omanut] _

word = 'אׇמָּנוּת', expected = 'ʔomanut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אׇמָּנוּת: got ʔomanˈut, expected ʔomanut
E       assert 'ʔomanˈut' == 'ʔomanut'
E         
E         - ʔomanut
E         + ʔomanˈut
E         ?      +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b4\u05ea\u05b0\u05d0\u05b7\u05d1\u05b0\u05bc\u05d3\u05d5\u05bc\u05ea-hit\u0294abd\u02c8ut] _

word = 'הִתְאַבְּדוּת', expected = 'hitʔabdˈut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הִתְאַבְּדוּת: got hitʔaudˈut, expected hitʔabdˈut
E       assert 'hitʔaudˈut' == 'hitʔabdˈut'
E         
E         - hitʔabdˈut
E         ?      ^
E         + hitʔaudˈut
E         ?      ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e6\u05b0\u05d1\u05b8\u05d0\u05b4\u05ab\u05d9-tsva\u0294\u02c8i] _

word = 'צְבָאִ֫י', expected = 'tsvaʔˈi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צְבָאִ֫י: got tsvaʔˈij, expected tsvaʔˈi
E       assert 'tsvaʔˈij' == 'tsvaʔˈi'
E         
E         - tsvaʔˈi
E         + tsvaʔˈij
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e6\u05b8\u05d4\u05b3\u05e8\u05b7\u05ab\u05d9\u05b4\u05dd-tsohor\u02c8ajim] _

word = 'צָהֳרַ֫יִם', expected = 'tsohorˈajim'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צָהֳרַ֫יִם: got tsahorˈajim, expected tsohorˈajim
E       assert 'tsahorˈajim' == 'tsohorˈajim'
E         
E         - tsohorˈajim
E         ?   ^
E         + tsahorˈajim
E         ?   ^

tests/test_phonemize.py:16: AssertionError
___ test_phonemize[\u05de\u05b4\u05d1\u05b0\u05e6\u05b8\u05e8-mivts\u02c8ar] ___

word = 'מִבְצָר', expected = 'mivtsˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מִבְצָר: got miutsˈar, expected mivtsˈar
E       assert 'miutsˈar' == 'mivtsˈar'
E         
E         - mivtsˈar
E         ?   ^
E         + miutsˈar
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05b4\u05ab\u05d9\u05de\u05b0\u05d9\u05b8\u05d4-x\u02c8imja] _

word = 'כִ֫ימְיָה', expected = 'xˈimja'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כִ֫ימְיָה: got xˈijmja, expected xˈimja
E       assert 'xˈijmja' == 'xˈimja'
E         
E         - xˈimja
E         + xˈijmja
E         ?    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d0\u05b5\u05d9\u05d1\u05b8\u05e8\u05b8\u05ab\u05d9\u05d5-\u0294ejvar\u02c8av] _

word = 'אֵיבָרָ֫יו', expected = 'ʔejvarˈav'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֵיבָרָ֫יו: got ʔejvarˈajv, expected ʔejvarˈav
E       assert 'ʔejvarˈajv' == 'ʔejvarˈav'
E         
E         - ʔejvarˈav
E         + ʔejvarˈajv
E         ?         +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d0\u05b4\u05d9\u05b8\u05bc\u05ab\u05e8-\u0294ij\u02c8ar1] _

word = 'אִיָּ֫ר', expected = 'ʔijˈar'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אִיָּ֫ר: got ʔˈiar, expected ʔijˈar
E       assert 'ʔˈiar' == 'ʔijˈar'
E         
E         - ʔijˈar
E         + ʔˈiar

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05bd\u05e9\u05c1\u05d5\u05b9\u05e0\u05b7\u05d0\u05d9-le\u0283on\u02c8aj] _

word = 'לֽשׁוֹנַאי', expected = 'leʃonˈaj'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לֽשׁוֹנַאי: got , expected leʃonˈaj
E       assert '' == 'leʃonˈaj'
E         
E         - leʃonˈaj

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 7 has multiple outgoing arcs
_ test_phonemize[\u05d0\u05b5\u05d9\u05e8\u05ab\u05d5\u05b9\u05e4\u05b8\u05bc\u05d4-\u0294ejr\u02c8opa] _

word = 'אֵיר֫וֹפָּה', expected = 'ʔejrˈopa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֵיר֫וֹפָּה: got ʔejrˈofa, expected ʔejrˈopa
E       assert 'ʔejrˈofa' == 'ʔejrˈopa'
E         
E         - ʔejrˈopa
E         ?       ^
E         + ʔejrˈofa
E         ?       ^

tests/test_phonemize.py:16: AssertionError
__ test_phonemize[\u05e4\u05b8\u05d0\u05e8\u05b0\u05e9\u05c1-f\u02c8ar\u0283] __

word = 'פָארְשׁ', expected = 'fˈarʃ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: פָארְשׁ: got , expected fˈarʃ
E       assert '' == 'fˈarʃ'
E         
E         - fˈarʃ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 17 has multiple outgoing arcs
_ test_phonemize[\u05e4\u05ab\u05d5\u05b9\u05d1\u05b0\u05bc\u05d9\u05b8\u05d4-f\u02c8obja] _

word = 'פ֫וֹבְּיָה', expected = 'fˈobja'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: פ֫וֹבְּיָה: got fˈouja, expected fˈobja
E       assert 'fˈouja' == 'fˈobja'
E         
E         - fˈobja
E         ?    ^
E         + fˈouja
E         ?    ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05b0\u05bc\u05ea\u05b9\u05ab\u05d1\u05b6\u05ea-kt\u02c8ovet] _

word = 'כְּתֹ֫בֶת', expected = 'ktˈovet'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כְּתֹ֫בֶת: got xtˈovet, expected ktˈovet
E       assert 'xtˈovet' == 'ktˈovet'
E         
E         - ktˈovet
E         ? ^
E         + xtˈovet
E         ? ^

tests/test_phonemize.py:16: AssertionError
________ test_phonemize[\u05e8\u05b9\u05d0\u05e9\u05c1-r\u02c8o\u0283] _________

word = 'רֹאשׁ', expected = 'rˈoʃ'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רֹאשׁ: got , expected rˈoʃ
E       assert '' == 'rˈoʃ'
E         
E         - rˈoʃ

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 12 has multiple outgoing arcs
_ test_phonemize[\u05e8\u05b4\u05d0\u05e9\u05c1\u05d5\u05b9\u05df-ri\u0283\u02c8on] _

word = 'רִאשׁוֹן', expected = 'riʃˈon'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: רִאשׁוֹן: got , expected riʃˈon
E       assert '' == 'riʃˈon'
E         
E         - riʃˈon

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 10 has multiple outgoing arcs
________ test_phonemize[\u05e6\u05b7\u05d4\u05b7"\u05dc-ts\u02c8ahal2] _________

word = 'צַהַ"ל', expected = 'tsˈahal'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צַהַ"ל: got , expected tsˈahal
E       assert '' == 'tsˈahal'
E         
E         - tsˈahal

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_________ test_phonemize[\u05e7\u05b5\u05e8\u05b5\u05d7\u05b7-kereax] __________

word = 'קֵרֵחַ', expected = 'kereax'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: קֵרֵחַ: got kereˈax, expected kereax
E       assert 'kereˈax' == 'kereax'
E         
E         - kereax
E         + kereˈax
E         ?     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b0\u05bd\u05e6\u05b7\u05d9\u05b5\u05bc\u05e8-letsajer] _

word = 'לְֽצַיֵּר', expected = 'letsajer'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לְֽצַיֵּר: got letsajˈer, expected letsajer
E       assert 'letsajˈer' == 'letsajer'
E         
E         - letsajer
E         + letsajˈer
E         ?       +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05db\u05b8\u05bc\u05dc\u05b0\u05bd\u05dc\u05b8\u05d4-kalela] _

word = 'כָּלְֽלָה', expected = 'kalela'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: כָּלְֽלָה: got xalelˈa, expected kalela
E       assert 'xalelˈa' == 'kalela'
E         
E         - kalela
E         ? ^
E         + xalelˈa
E         ? ^    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b7\u05dc\u05b0\u05bd\u05dc\u05d5\u05bc\u05d9\u05b8\u05d4\u05bc-haleluja] _

word = 'הַלְֽלוּיָהּ', expected = 'haleluja'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הַלְֽלוּיָהּ: got halelujˈa, expected haleluja
E       assert 'halelujˈa' == 'haleluja'
E         
E         - haleluja
E         + halelujˈa
E         ?        +

tests/test_phonemize.py:16: AssertionError
___ test_phonemize[\u05e1\u05b8\u05dc\u05b0\u05bd\u05dc\u05d5\u05bc-salelu] ____

word = 'סָלְֽלוּ', expected = 'salelu'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סָלְֽלוּ: got salˈelv, expected salelu
E       assert 'salˈelv' == 'salelu'
E         
E         - salelu
E         ?      ^
E         + salˈelv
E         ?    +  ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d4\u05b4\u05ea\u05b0\u05d1\u05bc\u05d5\u05b9\u05dc\u05b0\u05bd\u05dc\u05d5\u05bc\u05ea-hitbolelut] _

word = 'הִתְבּוֹלְֽלוּת', expected = 'hitbolelut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: הִתְבּוֹלְֽלוּת: got , expected hitbolelut
E       assert '' == 'hitbolelut'
E         
E         - hitbolelut

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: State 11 has multiple outgoing arcs
_ test_phonemize[\u05e9\u05c1\u05b6\u05d6\u05bc\u05b6\u05ab\u05d4-\u0283ez\u02c8e] _

word = 'שֶׁזֶּ֫ה', expected = 'ʃezˈe'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שֶׁזֶּ֫ה: got ʃezˈeh, expected ʃezˈe
E       assert 'ʃezˈeh' == 'ʃezˈe'
E         
E         - ʃezˈe
E         + ʃezˈeh
E         ?      +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d0\u05b5\u05d9\u05d1\u05b8\u05e8\u05b8\u05d9\u05d5-\u0294ejvar\u02c8av] _

word = 'אֵיבָרָיו', expected = 'ʔejvarˈav'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֵיבָרָיו: got ʔejvarˈajv, expected ʔejvarˈav
E       assert 'ʔejvarˈajv' == 'ʔejvarˈav'
E         
E         - ʔejvarˈav
E         + ʔejvarˈajv
E         ?         +

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05e1\u05b0\u05ea\u05b8\u05d9\u05d5-st\u02c8av] ________

word = 'סְתָיו', expected = 'stˈav'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סְתָיו: got stˈajv, expected stˈav
E       assert 'stˈajv' == 'stˈav'
E         
E         - stˈav
E         + stˈajv
E         ?     +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d7\u05b7\u05d9\u05b8\u05bc\u05d9\u05af\u05dc-xaj\u02c8al] _

word = 'חַיָּי֯ל', expected = 'xajˈal'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: חַיָּי֯ל: got , expected xajˈal
E       assert '' == 'xajˈal'
E         
E         - xajˈal

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05de\u05b7\u05e2\u05b0\u05d9\u05b8\u05d9\u05af\u05df-ma\u0294j\u02c8an] _

word = 'מַעְיָי֯ן', expected = 'maʔjˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מַעְיָי֯ן: got , expected maʔjˈan
E       assert '' == 'maʔjˈan'
E         
E         - maʔjˈan

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e2\u05b2\u05d9\u05b8\u05d9\u05af\u05e8\u05b8\u05d4-\u0294ajar\u02c8a] _

word = 'עֲיָי֯רָה', expected = 'ʔajarˈa'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עֲיָי֯רָה: got , expected ʔajarˈa
E       assert '' == 'ʔajarˈa'
E         
E         - ʔajarˈa

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05de\u05b0\u05bd\u05e2\u05bb\u05d5\u05af\u05d9\u05b8\u05bc\u05d9\u05af\u05df-me\u0294uj\u02c8an] _

word = 'מְֽעֻו֯יָּי֯ן', expected = 'meʔujˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽעֻו֯יָּי֯ן: got , expected meʔujˈan
E       assert '' == 'meʔujˈan'
E         
E         - meʔujˈan

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e1\u05b4\u05d9\u05af\u05ab\u05d9\u05b7\u05bc\u05de\u05b0\u05ea\u05b4\u05bc\u05d9-sij\u02c8amti] _

word = 'סִי֯֫יַּמְתִּי', expected = 'sijˈamti'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סִי֯֫יַּמְתִּי: got , expected sijˈamti
E       assert '' == 'sijˈamti'
E         
E         - sijˈamti

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e2\u05b5\u05d9\u05e0\u05b7\u05d9\u05af\u05d9-\u0294en\u02c8aj] _

word = 'עֵינַי֯י', expected = 'ʔenˈaj'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: עֵינַי֯י: got , expected ʔenˈaj
E       assert '' == 'ʔenˈaj'
E         
E         - ʔenˈaj

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05de\u05b0\u05bd\u05e7\u05bb\u05d5\u05dc\u05b8\u05bc\u05e3-mekul\u02c8af] _

word = 'מְֽקֻולָּף', expected = 'mekulˈaf'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽקֻולָּף: got mekuulˈaf, expected mekulˈaf
E       assert 'mekuulˈaf' == 'mekulˈaf'
E         
E         - mekulˈaf
E         + mekuulˈaf
E         ?    +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e9\u05bb\u05c1\u05d5\u05af\u05dc\u05b0\u05d7\u05b8\u05df-\u0283ulx\u02c8an] _

word = 'שֻׁו֯לְחָן', expected = 'ʃulxˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: שֻׁו֯לְחָן: got , expected ʃulxˈan
E       assert '' == 'ʃulxˈan'
E         
E         - ʃulxˈan

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d8\u05b0\u05e8\u05b7\u05d0\u05af\u05de\u05b0\u05e4\u05bc-tr\u02c8amp] _

word = 'טְרַא֯מְפּ', expected = 'trˈamp'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: טְרַא֯מְפּ: got , expected trˈamp
E       assert '' == 'trˈamp'
E         
E         - trˈamp

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05d0\u05b2\u05d5\u05b4\u05d5\u05d9\u05e8-\u0294av\u02c8ir] __

word = 'אֲוִויר', expected = 'ʔavˈir'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֲוִויר: got ʔaviˈujr, expected ʔavˈir
E       assert 'ʔaviˈujr' == 'ʔavˈir'
E         
E         - ʔavˈir
E         + ʔaviˈujr

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05d0\u05b2\u05d5\u05b0\u05d5\u05e8\u05b4\u05d9\u05e8\u05b4\u05d9-\u0294avrir\u02c8i] _

word = 'אֲוְורִירִי', expected = 'ʔavrirˈi'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: אֲוְורִירִי: got ʔavurirˈi, expected ʔavrirˈi
E       assert 'ʔavurirˈi' == 'ʔavrirˈi'
E         
E         - ʔavrirˈi
E         + ʔavurirˈi
E         ?    +

tests/test_phonemize.py:16: AssertionError
______ test_phonemize[\u05e6\u05b8\u05d4\u05b9\u05d5\u05d1-tsah\u02c8ov] _______

word = 'צָהֹוב', expected = 'tsahˈov'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: צָהֹוב: got tsahˈovv, expected tsahˈov
E       assert 'tsahˈovv' == 'tsahˈov'
E         
E         - tsahˈov
E         + tsahˈovv
E         ?        +

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05dc\u05b4\u05d5\u05b0\u05d9\u05b8\u05ea\u05b8\u05df-livjat\u02c8an1] _

word = 'לִוְיָתָן', expected = 'livjatˈan'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לִוְיָתָן: got liujatˈan, expected livjatˈan
E       assert 'liujatˈan' == 'livjatˈan'
E         
E         - livjatˈan
E         ?   ^
E         + liujatˈan
E         ?   ^

tests/test_phonemize.py:16: AssertionError
_______ test_phonemize[\u05d8\u05b7\u05d5\u05b8\u05d5\u05e1-tav\u02c8as] _______

word = 'טַוָוס', expected = 'tavˈas'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: טַוָוס: got tavaˈus, expected tavˈas
E       assert 'tavaˈus' == 'tavˈas'
E         
E         - tavˈas
E         ?     ^
E         + tavaˈus
E         ?    + ^

tests/test_phonemize.py:16: AssertionError
_ test_phonemize[\u05e0\u05b4\u05d9\u05af\u05d5\u05bc\u05d5\u05bc\u05d8-niv\u02c8ut] _

word = 'נִי֯וּוּט', expected = 'nivˈut'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: נִי֯וּוּט: got , expected nivˈut
E       assert '' == 'nivˈut'
E         
E         - nivˈut

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05e1\u05b4\u05d9\u05af\u05d5\u05bc\u05d5\u05bc\u05d2-siv\u02c8ug] _

word = 'סִי֯וּוּג', expected = 'sivˈug'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: סִי֯וּוּג: got , expected sivˈug
E       assert '' == 'sivˈug'
E         
E         - sivˈug

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05ea\u05b4\u05bc\u05d9\u05af\u05d5\u05bc\u05d5\u05bc\u05da\u05b0-tiv\u02c8ux] _

word = 'תִּי֯וּוּךְ', expected = 'tivˈux'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: תִּי֯וּוּךְ: got , expected tivˈux
E       assert '' == 'tivˈux'
E         
E         - tivˈux

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05de\u05b0\u05bd\u05e7\u05bb\u05d5\u05b6\u05bc\u05ab\u05d5\u05af\u05e0\u05b6\u05ea-mekuv\u02c8enet] _

word = 'מְֽקֻוֶּ֫ו֯נֶת', expected = 'mekuvˈenet'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽקֻוֶּ֫ו֯נֶת: got , expected mekuvˈenet
E       assert '' == 'mekuvˈenet'
E         
E         - mekuvˈenet

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05de\u05b0\u05bd\u05e1\u05bb\u05d5\u05b6\u05bc\u05ab\u05d5\u05af\u05d2\u05b6\u05ea-mesuv\u02c8eget] _

word = 'מְֽסֻוֶּ֫ו֯גֶת', expected = 'mesuvˈeget'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: מְֽסֻוֶּ֫ו֯גֶת: got , expected mesuvˈeget
E       assert '' == 'mesuvˈeget'
E         
E         - mesuvˈeget

tests/test_phonemize.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: StringFstToOutputLabels: Invalid start state
_ test_phonemize[\u05dc\u05b0\u05bd\u05db\u05b7\u05d5\u05bc\u05b5\u05d5\u05df-lexaven] _

word = 'לְֽכַוֵּון', expected = 'lexaven'

    @pytest.mark.parametrize("word,expected", df.values.tolist())
    def test_phonemize(word, expected):
        got = phonemize(word)
>       assert got == expected, f"{word}: got {got}, expected {expected}"
E       AssertionError: לְֽכַוֵּון: got lexaveˈun, expected lexaven
E       assert 'lexaveˈun' == 'lexaven'
E         
E         - lexaven
E         + lexaveˈun
E         ?       ++

tests/test_phonemize.py:16: AssertionError
=========================== short test summary info ============================
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05c7\u05dc-k\u02c8ol]
FAILED tests/test_phonemize.py::test_phonemize[\u05d9\u05b4\u05e9\u05c2\u05b0\u05e8\u05b8\u05d0\u05b5\u05dc-jisra\u0294\u02c8el]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b7\u05db\u05b6\u05bc\u05ab\u05d1\u05b6\u05dc-rak\u02c8evel]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b5\u05ab\u05d9\u05d7\u05b7-r\u02c8eax]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05b7\u05bc\u05ab\u05d9\u05b4\u05ea-b\u02c8ajit]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05c2\u05b7\u05ab\u05de\u05b0\u05ea\u05bc\u05b8-s\u02c8amta]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b8\u05bc\u05d0\u05df-k\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b7\u05d5\u05b7\u05bc\u05d0\u05e8-tsav\u02c8ar]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05d5\u05b0\u05d9\u05b8\u05ea\u05b8\u05df-livjat\u02c8an0]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b8\u05d0\u05b2\u05d1\u05b8\u05d4-ka\u0294av\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b4\u05e1\u05b0\u05e2\u05b4\u05ab\u05d9\u05e8\u05d5\u05bc-his\u0294\u02c8iru]
FAILED tests/test_phonemize.py::test_phonemize[\u05d6\u05b9\u05d0\u05ea-z\u02c8ot]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b8\u05d0\u05e9\u05c1\u05b4\u05d9-ra\u0283\u02c8i]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b8\u05e2\u05b2\u05e8\u05d5\u05bc-ba\u0294ar\u02c8u]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b4\u05e8\u05b0\u05e2\u05b2\u05e8\u05d5\u05bc-\u0294ir\u0294ar\u02c8u]
FAILED tests/test_phonemize.py::test_phonemize[\u05d7\u05b2\u05ea\u05bb\u05d5\u05e0\u05bc\u05b8\u05d4-xatun\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05d7\u05b3\u05d3\u05b8\u05e9\u05c1\u05b4\u05ab\u05d9\u05dd-xoda\u0283\u02c8im0]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b0\u05e4\u05d5\u05bc\u05e8\u05b4\u05ab\u05d9\u05dd-sfur\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b8\u05ab\u05da\u05b0-k\u02c8ax0]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d0\u05b4\u05e9\u05bc\u05c1\u05ab\u05d5\u05bc\u05dd-be\u0294i\u0283\u02c8um]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b7\u05db\u05bc\u05b6\u05ab\u05e1\u05b6\u05e3-hak\u02c8esef]
FAILED tests/test_phonemize.py::test_phonemize[\u05d5\u05b0\u05bd\u05d4\u05b7\u05e1\u05bc\u05b0\u05d8\u05b7\u05ab\u05e8\u05b0\u05d8\u05b0\u05d0\u05b7\u05e4\u05bc-vehast\u02c8art\u0294ap]
FAILED tests/test_phonemize.py::test_phonemize[\u05e0\u05b4\u05de\u05b0\u05db\u05bc\u05b7\u05ab\u05e8-nimk\u02c8ar]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d4\u05b6\u05e4\u05b0\u05e1\u05b5\u05ab\u05d3-behefs\u02c8ed]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b4\u05de\u05b0\u05e2\u05b7\u05ab\u05d8-kim\u0294\u02c8at]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b7\u05e1\u05b0\u05e4\u05bc\u05b5\u05ab\u05d9-kasp\u02c8ej]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b7\u05de\u05bc\u05b7\u05e9\u05c1\u05b0\u05e7\u05b4\u05d9\u05e2\u05b4\u05ab\u05d9\u05dd-hama\u0283ki\u0294\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b4\u05e9\u05c1\u05b0\u05ea\u05bc\u05b7\u05de\u05bc\u05b5\u05ab\u05e9\u05c1-hi\u0283tam\u02c8e\u0283]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b7\u05de\u05bc\u05b5\u05d0\u05ab\u05d5\u05b9\u05ea-bame\u0294\u02c8ot]
FAILED tests/test_phonemize.py::test_phonemize[\u05e7\u05b7\u05d1\u05bc\u05b0\u05dc\u05b8\u05e0\u05b4\u05ab\u05d9\u05dd-kablan\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b0\u05bd\u05db\u05b4\u05d9\u05e9\u05c1\u05b8\u05ab\u05d4-rexi\u0283\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d1\u05b4\u05e0\u05b0\u05d9\u05b7\u05ab\u05df-bevinj\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b4\u05e9\u05c2\u05b0\u05e8\u05b8\u05d3\u05b4\u05ab\u05d9\u05dd-misrad\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05e4\u05b4\u05d9\u05dc\u05b4\u05d9\u05e4\u05bc\u05b4\u05ab\u05d9\u05e0\u05b4\u05d9\u05dd-befilip\u02c8inim]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b0\u05bd\u05d3\u05b5\u05ab\u05d9-ked\u02c8ej]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b0\u05bd\u05d4\u05b7\u05e9\u05c1\u05b0\u05dc\u05b4\u05ab\u05d9\u05dd-leha\u0283l\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d9\u05b0\u05d3\u05b8\u05e0\u05b4\u05ab\u05d9\u05ea-jdan\u02c8it]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05c1\u05b6\u05d1\u05bc\u05bb\u05e6\u05bc\u05b0\u05e2\u05ab\u05d5\u05bc-\u0283ebuts\u0294\u02c8u]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b8\u05d0\u05b7\u05e4\u05bc\u05b0\u05dc\u05b4\u05d9\u05e7\u05b7\u05ab\u05e6\u05b0\u05d9\u05b8\u05d4-ha\u0294aplik\u02c8atsja]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b7\u05d4\u05d5\u05b9\u05d3\u05b8\u05e2\u05b8\u05ab\u05d4-bahoda\u0294\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b0\u05ea\u05b7\u05ab\u05d1-kt\u02c8av]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b4\u05e9\u05c2\u05b0\u05e8\u05b7\u05ab\u05d3-misr\u02c8ad]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b7\u05de\u05bc\u05b4\u05e9\u05c1\u05b0\u05e4\u05bc\u05b8\u05d8\u05b4\u05ab\u05d9\u05dd-hami\u0283pat\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d0\u05b5\u05d6\u05ab\u05d5\u05b9\u05e8-be\u0294ez\u02c8or]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b7\u05d7\u05b7\u05d2\u05bc\u05b4\u05ab\u05d9\u05dd-haxag\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b8\u05e2\u05b2\u05de\u05d5\u05bc\u05e1\u05b8\u05ab\u05d4-ha\u0294amus\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b4\u05e1\u05b0\u05e4\u05bc\u05b7\u05ab\u05e8-misp\u02c8ar]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b8\u05ab\u05da\u05b0-k\u02c8ax1]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b9\u05ab\u05d0-l\u02c8o]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b4\u05e9\u05c1\u05b0\u05ea\u05bc\u05b7\u05de\u05bc\u05b5\u05ab\u05e9\u05c1-mi\u0283tam\u02c8e\u0283]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05b0\u05bd\u05d1\u05ab\u05d5\u05b9\u05d8\u05b4\u05d9\u05dd-bev\u02c8otim]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05bc\u05ab\u05d5\u05b9\u05d8\u05b4\u05d9\u05dd-b\u02c8otim]
FAILED tests/test_phonemize.py::test_phonemize[\u05d8\u05b4\u05e4\u05bc\u05b0\u05e9\u05c1\u05b4\u05ab\u05d9\u05dd-tip\u0283\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05bc\u05b0\u05e4\u05b4\u05ab\u05d9-kf\u02c8i]
FAILED tests/test_phonemize.py::test_phonemize[\u05e7\u05b8\u05e8\u05b8\u05ab\u05d0-kar\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05c1\u05d5\u05bc\u05dc\u05b7\u05de\u05bc\u05b4\u05ab\u05d9\u05ea-\u0283ulam\u02c8it]
FAILED tests/test_phonemize.py::test_phonemize[\u05d9\u05b7\u05d3\u05b8\u05e0\u05b4\u05ab\u05d9\u05ea-jadan\u02c8it]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b4\u05e8\u05b0\u05d8\u05d5\u05b9\u05e0\u05b4\u05ab\u05d9\u05dd-sirton\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05d5\u05b9\u05e4\u05b4\u05ab\u05d9\u05dd-tsof\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d2\u05bc\u05b0\u05d3\u05b4\u05d9\u05dc\u05b8\u05ab\u05d4-gdil\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05e4\u05bc\u05b4\u05ea\u05bc\u05ab\u05d5\u05bc\u05d7\u05b7-pit\u02c8uax]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b4\u05d2\u05bc'\u05d5\u05b9\u05e0\u05b0\u05e8\u05b8\u05d8\u05b4\u05ab\u05d9\u05dd-mid\u0292onrat\u02c8im]
FAILED tests/test_phonemize.py::test_phonemize[\u05d6\u05b8'\u05e7\u05b5\u05ab\u05d8-\u0292ak\u02c8et]
FAILED tests/test_phonemize.py::test_phonemize[\u05d7\u05b3\u05d3\u05b8\u05e9\u05c1\u05b4\u05ab\u05d9\u05dd-xoda\u0283\u02c8im1]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b2\u05d1\u05d5\u05b9\u05d3\u05b8\u05ab\u05d4-\u0294avod\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b7\u05e1\u05b0\u05e4\u05bc\u05b4\u05ab\u05d9\u05e7-masp\u02c8ik]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b5\u05ab\u05dc\u05bc\u05d5\u05bc-\u0294\u02c8elu]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b0\u05bd\u05d4\u05b4\u05db\u05bc\u05b8\u05e9\u05c1\u05b5\u05ab\u05dc-lehika\u0283\u02c8el]
FAILED tests/test_phonemize.py::test_phonemize[\u05ea\u05bc\u05b7\u05e4\u05b0\u05e7\u05b4\u05ab\u05d9\u05d3-tafk\u02c8id]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05e9\u05c2\u05b4\u05d9\u05de\u05b8\u05ab\u05d4-mesim\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05e6\u05bb\u05e4\u05bc\u05b6\u05ab\u05d4-metsup\u02c8e]
FAILED tests/test_phonemize.py::test_phonemize[\u05d2\u05bc\u05ab'\u05d5\u05bc\u05e0\u05b0\u05d9\u05d5\u05b9\u05e8-d\u0292\u02c8unjor]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b4\u05d9\u05b8\u05bc\u05ab\u05e8-\u0294ij\u02c8ar0]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05b7\u05c2\u05de\u05b0\u05ea\u05b8\u05bc-samta]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b7\u05d4\u05b7\u05f4\u05dc-ts\u02c8ahal]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b7\u05d4\u05b7"\u05dc-ts\u02c8ahal0]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b7\u05bc\u05d4\u05b2\u05dc\u05b8\u05db\u05b8\u05d4-kahalax\u02c8a0]
FAILED tests/test_phonemize.py::test_phonemize[\u05ea\u05b8\u05bc\u05de\u05d5\u05bc\u05d4\u05b7\u05bc-tamu\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05d2\u05b8\u05bc\u05d1\u05d5\u05b9\u05d4\u05b7\u05bc-gavo\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05c2\u05b4\u05d9\u05d7\u05b7-si\u02c8ax]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b9\u05ab\u05e2\u05b7-l\u02c8oa]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05e9\u05b0\u05c1\u05e7\u05b9\u05e2\u05b7-li\u0283koa]
FAILED tests/test_phonemize.py::test_phonemize[\u05e7\u05b8\u05dc\u05b4\u05d9\u05e2\u05b7-kalia]
FAILED tests/test_phonemize.py::test_phonemize[\u05e4\u05b8\u05bc\u05e8\u05d5\u05bc\u05e2\u05b7-parua]
FAILED tests/test_phonemize.py::test_phonemize[\u05e7\u05b8\u05dc\u05b0\u05e2\u05b8\u05d4-kal\u0294a]
FAILED tests/test_phonemize.py::test_phonemize[\u05e7\u05b8\u05e8\u05b0\u05d0\u05b8\u05d4-kar\u0294a]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05d2\u05bb\u05d5\u05b8\u05bc\u05df-meguvan0]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b4\u05d5\u05bc\u05d5\u05bc\u05ea-\u0294ivut0]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b4\u05d9\u05bc\u05d5\u05bc\u05ea-\u0294ijut0]
FAILED tests/test_phonemize.py::test_phonemize[\u05d5\u05b0\u05d4\u05b4\u05ea\u05b0\u05d7\u05b4\u05d9\u05dc-vehitxil]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b2\u05d2\u05b7\u05e0\u05b8\u05bc\u05d4-hagana]
FAILED tests/test_phonemize.py::test_phonemize[\u05d8\u05b7\u05d5\u05bc\u05b8\u05e1-tavas]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b4\u05d5\u05bc\u05b5\u05e8-\u0294iver]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b8\u05d5\u05d5\u05b9\u05df-\u0294avon]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05d2\u05b0\u05d5\u05b9\u05e2\u05b7-ligvoa]
FAILED tests/test_phonemize.py::test_phonemize[\u05d5\u05d5\u05b9\u05dc\u05b0\u05d8-volt]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05d2\u05bb\u05d5\u05b8\u05bc\u05df-meguvan1]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b4\u05d5\u05bc\u05d5\u05bc\u05ea-\u0294ivut1]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b4\u05d9\u05bc\u05d5\u05bc\u05ea-\u0294ijut1]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05d5\u05b0\u05d9\u05b8\u05ea\u05b8\u05ab\u05df-livjat\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b7\u05db\u05b0\u05e9\u05c1\u05b8\u05ab\u05d9\u05d5-\u0294ax\u0283\u02c8av]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05ab\u05d5\u05b9\u05dc\u05b6\u05e8\u05b0\u05d1\u05b0\u05bc\u05dc\u05b6\u05d9\u05b0\u05d3\u05b0\u05e1-r\u02c8olerblejds]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b8\u05ab\u05de\u05b8"\u05d7-r\u02c8amax]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b7\u05d4\u05b7"\u05dc-ts\u02c8ahal1]
FAILED tests/test_phonemize.py::test_phonemize[\u05d9\u05b4\u05e9\u05b8\u05bc\u05c2\u05e9\u05db\u05b8\u05ab\u05e8-jisax\u02c8ar]
FAILED tests/test_phonemize.py::test_phonemize[\u05d5\u05b7\u05e1\u05b7\u05d1\u05b4\u05bc\u05d9-was\u02c8abi]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b7\u05bc\u05d4\u05b2\u05dc\u05b8\u05db\u05b8\u05d4-kahalax\u02c8a1]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b8\u05d6\u05b6\u05e8\u05b0\u05d1\u05b7\u05bc\u05d9\u05b0\u05d2\u05b8'\u05df-\u0294azerbajd\u0292\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b5\u05ab\u05e8\u05d5\u05b9\u05d2\u05b6'\u05dc-\u0294\u02c8erod\u0292el]
FAILED tests/test_phonemize.py::test_phonemize[\u05d2'\u05d5\u05b9\u05d1\u05bc-d\u0292\u02c8ob]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b8\u05d2\u05b6\u05ab'\u05e0\u05b0\u05d3\u05b8\u05d4-\u0294ad\u0292\u02c8enda]
FAILED tests/test_phonemize.py::test_phonemize[\u05e4\u05b4\u05bc\u05d9\u05d2\u05b8\u05ab'\u05de\u05b8\u05d4-pid\u0292\u02c8ama]
FAILED tests/test_phonemize.py::test_phonemize[\u05d8\u05b0\u05e8\u05b7\u05e0\u05b0\u05e1\u05b0\u05d2\u05b6\u05ab'\u05e0\u05b0\u05d3\u05b6\u05bc\u05e8-transd\u0292\u02c8ender]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b4'\u05d9\u05e4\u05b0\u05bc\u05e1-t\u0283\u02c8ips]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05ab\u05d9\u05e6\u05b4'\u05d9-l\u02c8it\u0283i]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05ab\u05d9\u05e0\u05b0\u05e5'-l\u02c8int\u0283]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b7\u05ab'\u05e8\u05b0\u05d8\u05b6\u05e8-t\u0283\u02c8arter]
FAILED tests/test_phonemize.py::test_phonemize[\u05d1\u05b8\u05bc\u05d2\u05b8\u05d6'-bag\u02c8a\u0292]
FAILED tests/test_phonemize.py::test_phonemize[\u05d6\u05b7'\u05d1\u05bc\u05d5\u05b9\u05d8\u05b4\u05ab\u05d9\u05e0\u05b0\u05e1\u05b0\u05e7\u05b4\u05d9-\u0292abot\u02c8inski]
FAILED tests/test_phonemize.py::test_phonemize[\u05d5\u05b4\u05d9\u05d8\u05b0\u05e8\u05b8\u05d6'-vitr\u02c8a\u0292]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b0\u05bc\u05e1\u05b4\u05d9\u05dc-ks\u02c8il]
FAILED tests/test_phonemize.py::test_phonemize[\u05d2\u05b4'\u05d9\u05e4\u05bc-d\u0292\u02c8ip]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05c7\u05d7\u05b0\u05d1\u05bc\u05b4\u05d9-roxb\u02c8i]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b7\u05e6\u05b0\u05dc\u05b4\u05ab\u05d9\u05d7\u05b7-matsl\u02c8iax]
FAILED tests/test_phonemize.py::test_phonemize[\u05d8\u05b0\u05e8\u05b6\u05de\u05b0\u05e4\u05b0\u05bc-tr\u02c8emp]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b7\u05bc\u05d1\u05b8\u05bc\u05d1\u05bc-kab\u02c8ab]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b6\u05dc\u05b6\u05d1\u05bc-sel\u02c8eb]
FAILED tests/test_phonemize.py::test_phonemize[\u05e4\u05b8\u05bc\u05d0\u05d1\u05bc-p\u02c8ab]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05c7\u05de\u05bc\u05b8\u05e0\u05d5\u05bc\u05ea-\u0294omanut]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b4\u05ea\u05b0\u05d0\u05b7\u05d1\u05b0\u05bc\u05d3\u05d5\u05bc\u05ea-hit\u0294abd\u02c8ut]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b0\u05d1\u05b8\u05d0\u05b4\u05ab\u05d9-tsva\u0294\u02c8i]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b8\u05d4\u05b3\u05e8\u05b7\u05ab\u05d9\u05b4\u05dd-tsohor\u02c8ajim]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b4\u05d1\u05b0\u05e6\u05b8\u05e8-mivts\u02c8ar]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b4\u05ab\u05d9\u05de\u05b0\u05d9\u05b8\u05d4-x\u02c8imja]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b5\u05d9\u05d1\u05b8\u05e8\u05b8\u05ab\u05d9\u05d5-\u0294ejvar\u02c8av]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b4\u05d9\u05b8\u05bc\u05ab\u05e8-\u0294ij\u02c8ar1]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05bd\u05e9\u05c1\u05d5\u05b9\u05e0\u05b7\u05d0\u05d9-le\u0283on\u02c8aj]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b5\u05d9\u05e8\u05ab\u05d5\u05b9\u05e4\u05b8\u05bc\u05d4-\u0294ejr\u02c8opa]
FAILED tests/test_phonemize.py::test_phonemize[\u05e4\u05b8\u05d0\u05e8\u05b0\u05e9\u05c1-f\u02c8ar\u0283]
FAILED tests/test_phonemize.py::test_phonemize[\u05e4\u05ab\u05d5\u05b9\u05d1\u05b0\u05bc\u05d9\u05b8\u05d4-f\u02c8obja]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b0\u05bc\u05ea\u05b9\u05ab\u05d1\u05b6\u05ea-kt\u02c8ovet]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b9\u05d0\u05e9\u05c1-r\u02c8o\u0283]
FAILED tests/test_phonemize.py::test_phonemize[\u05e8\u05b4\u05d0\u05e9\u05c1\u05d5\u05b9\u05df-ri\u0283\u02c8on]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b7\u05d4\u05b7"\u05dc-ts\u02c8ahal2]
FAILED tests/test_phonemize.py::test_phonemize[\u05e7\u05b5\u05e8\u05b5\u05d7\u05b7-kereax]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b0\u05bd\u05e6\u05b7\u05d9\u05b5\u05bc\u05e8-letsajer]
FAILED tests/test_phonemize.py::test_phonemize[\u05db\u05b8\u05bc\u05dc\u05b0\u05bd\u05dc\u05b8\u05d4-kalela]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b7\u05dc\u05b0\u05bd\u05dc\u05d5\u05bc\u05d9\u05b8\u05d4\u05bc-haleluja]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b8\u05dc\u05b0\u05bd\u05dc\u05d5\u05bc-salelu]
FAILED tests/test_phonemize.py::test_phonemize[\u05d4\u05b4\u05ea\u05b0\u05d1\u05bc\u05d5\u05b9\u05dc\u05b0\u05bd\u05dc\u05d5\u05bc\u05ea-hitbolelut]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05c1\u05b6\u05d6\u05bc\u05b6\u05ab\u05d4-\u0283ez\u02c8e]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b5\u05d9\u05d1\u05b8\u05e8\u05b8\u05d9\u05d5-\u0294ejvar\u02c8av]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b0\u05ea\u05b8\u05d9\u05d5-st\u02c8av]
FAILED tests/test_phonemize.py::test_phonemize[\u05d7\u05b7\u05d9\u05b8\u05bc\u05d9\u05af\u05dc-xaj\u02c8al]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b7\u05e2\u05b0\u05d9\u05b8\u05d9\u05af\u05df-ma\u0294j\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b2\u05d9\u05b8\u05d9\u05af\u05e8\u05b8\u05d4-\u0294ajar\u02c8a]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05e2\u05bb\u05d5\u05af\u05d9\u05b8\u05bc\u05d9\u05af\u05df-me\u0294uj\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b4\u05d9\u05af\u05ab\u05d9\u05b7\u05bc\u05de\u05b0\u05ea\u05b4\u05bc\u05d9-sij\u02c8amti]
FAILED tests/test_phonemize.py::test_phonemize[\u05e2\u05b5\u05d9\u05e0\u05b7\u05d9\u05af\u05d9-\u0294en\u02c8aj]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05e7\u05bb\u05d5\u05dc\u05b8\u05bc\u05e3-mekul\u02c8af]
FAILED tests/test_phonemize.py::test_phonemize[\u05e9\u05bb\u05c1\u05d5\u05af\u05dc\u05b0\u05d7\u05b8\u05df-\u0283ulx\u02c8an]
FAILED tests/test_phonemize.py::test_phonemize[\u05d8\u05b0\u05e8\u05b7\u05d0\u05af\u05de\u05b0\u05e4\u05bc-tr\u02c8amp]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b2\u05d5\u05b4\u05d5\u05d9\u05e8-\u0294av\u02c8ir]
FAILED tests/test_phonemize.py::test_phonemize[\u05d0\u05b2\u05d5\u05b0\u05d5\u05e8\u05b4\u05d9\u05e8\u05b4\u05d9-\u0294avrir\u02c8i]
FAILED tests/test_phonemize.py::test_phonemize[\u05e6\u05b8\u05d4\u05b9\u05d5\u05d1-tsah\u02c8ov]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b4\u05d5\u05b0\u05d9\u05b8\u05ea\u05b8\u05df-livjat\u02c8an1]
FAILED tests/test_phonemize.py::test_phonemize[\u05d8\u05b7\u05d5\u05b8\u05d5\u05e1-tav\u02c8as]
FAILED tests/test_phonemize.py::test_phonemize[\u05e0\u05b4\u05d9\u05af\u05d5\u05bc\u05d5\u05bc\u05d8-niv\u02c8ut]
FAILED tests/test_phonemize.py::test_phonemize[\u05e1\u05b4\u05d9\u05af\u05d5\u05bc\u05d5\u05bc\u05d2-siv\u02c8ug]
FAILED tests/test_phonemize.py::test_phonemize[\u05ea\u05b4\u05bc\u05d9\u05af\u05d5\u05bc\u05d5\u05bc\u05da\u05b0-tiv\u02c8ux]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05e7\u05bb\u05d5\u05b6\u05bc\u05ab\u05d5\u05af\u05e0\u05b6\u05ea-mekuv\u02c8enet]
FAILED tests/test_phonemize.py::test_phonemize[\u05de\u05b0\u05bd\u05e1\u05bb\u05d5\u05b6\u05bc\u05ab\u05d5\u05af\u05d2\u05b6\u05ea-mesuv\u02c8eget]
FAILED tests/test_phonemize.py::test_phonemize[\u05dc\u05b0\u05bd\u05db\u05b7\u05d5\u05bc\u05b5\u05d5\u05df-lexaven]
======================= 173 failed, 105 passed in 0.48s ========================
