listOfIds = [
    "qysdgimlcaghpfozuwejmhrbvx", "qysdtiklcagnpfhzuwbjmhrtvx", "qysdtiflcsgnpfozuwejmhruvx", "qkshtiklnagnpfozuwejmhrbvx",
    "qysdtnklcagnpmozuwejmhrrvx", "qysdttkecagnpfozuwijmhrbvx", "qyedtiklcagnvfozuweymhrbvx", "qyzdtikzcagnpfozuwejmhqbvx",
    "qysdtiklcagnpfozlwedmhqbvx", "qjsdtiklcagnpfozubejmhrbvq", "qysdtiklcagnpfozvvejmhrbex", "qdsdziklcagnpfouuwejmhrbvx",
    "qysttikqccgnpfozuwejmhrbvx", "qysdtiklcagnpbozwwecmhrbvx", "qysdtiklcagnpfozuwexmmrjvx", "nysdtiklcqgjpfozuwejmhrbvx",
    "cysdoiqlcagnpfozuwejmhrbvx", "qysdthxlcagnpfozuwejmcrbvx", "qyswtiklcrgnpfozuwejmhrbvf", "qysdtiklcagnpfozurejmhvpvx",
    "qysdtiklcegnpfdzuwejghrbvx", "qysdtjkluagnpfozuwenmhrbvx", "qysdtimlcagnpjwzuwejmhrbvx", "qyrdtiklcegnpeozuwejmhrbvx",
    "qysdmiklcagnpfokswejmhrbvx", "qysdtizlcagnpiozuwecmhrbvx", "qysdtiklcignafxzuwejmhrbvx", "qycdjiklcagnpzozuwejmhrbvx",
    "qysdtiklcagnpjozuwepihrbvx", "qyedtiklcrgnpfozuvejmhrbvx", "mysdtikrcagnpfozwwejmhrbvx", "qysdtiklcagnpfozuhcjmhrbsx",
    "qmsdtiklcagnpfozuwehmhrevx", "qgsdtiklcagnpfozuwejvhrbvp", "lysdtikleagnpfozuwejmhrnvx", "qxsdtivlzagnpfozuwejmhrbvx",
    "qysdtiklcoggpfozuwebmhrbvx", "wysdtiklcagnpfozuwejmornvx", "jysdtiklvagntfozuwejmhrbvx", "qmsdtiklcagnpfozuwejmrrbax",
    "qysdttklcagnpfoiuwejmhrbvh", "qysdtnklcaenpfozupejmhrbvx", "qysdtoklcagnpfozuwexmhrbvq", "qysdtiklcagnpuoeuwejmhrjvx",
    "iysdtitncagnpfozuwejmhrbvx", "qysdtixrcagnprozuwejmhrbvx", "qyfdtiplcagnpfouuwejmhrbvx", "qysdtmklcagnpfowuwejmhrbox",
    "qysdtiklcagnxiozuwejphrbvx", "fysdtiklcagnptozuwejmhrbvo", "qysdqiklcagnplozuwejmhmbvx", "qysdtwkacagnpfosuwejmhrbvx",
    "qysdtitlcagnpfozufajmhrbvx", "qysdtcklcagopfdzuwejmhrbvx", "qmfdtdklcagnpfozuwejmhrbvx", "qysztiklcaonpfozuwejmhrbfx",
    "qygdtiklcggnpfozuwejmhrhvx", "qysdiiklcagnpfozukejmcrbvx", "qysdtrkloagnpfozuwujmhrbvx", "qycdtiklcagnpfozywejmhrlvx",
    "qgsdtikdcagnpfozgwejmhrbvx", "qyudtikleagvpfozuwejmhrbvx", "pysdtiqlcagnpfozuwejmarbvx", "qysdtiklcaenpfozuwehahrbvx",
    "qhsttiklcagnpfovuwejmhrbvx", "zysdtikqmagnpfozuwejmhrbvx", "rysdtikacagnpfozuwevmhrbvx", "zysntikllagnpfozuwejmhrbvx",
    "qysttimlcagndfozuwejmhrbvx", "qysdtiklcaxopfqzuwejmhrbvx", "qysdtislcagnpfozuwejmtrbnx", "qysdviklcagnpfozswejmhibvx",
    "qmsdtiklrygnpfozuwejmhrbvx", "qysztiklcagnpfozuwejmorbrx", "xysdtiklcagnzwozuwejmhrbvx", "qysjthklcagnpfozowejmhrbvx",
    "qysdtiklcagnpfofxwemmhrbvx", "jysdtiklcagnpfozfwehmhrbvx", "qysdtgklaagnpfozhwejmhrbvx", "qqsdtiklcaenpfozuwejmhrvvx",
    "qysdtikloajppfozuwejmhrbvx", "qysdtiklcagnpwozuwejmhrhsx", "qpsdtiklcapnprozuwejmhrbvx", "qyzdtiklcagnpcozuwejmhrbvc",
    "qusdhiklcagnpfozuwejmhrbxx", "qysdtiklcagnpfozqwejthrvvx", "qysvtiklcagnpfoiuwedmhrbvx", "qgsdtiklcagvpfozuwejmhrbvf",
    "qysdtikxcawnpfozuwejmarbvx", "qyvctiklcaynpfozuwejmhrbvx", "qyyltiklnagnpfozuwejmhrbvx", "oysdtillcagnpfozuwejmnrbvx",
    "qysdtiklcagnpfozuvmjmhrbzx", "qykdtikocagnpfhzuwejmhrbvx", "qysdtvkloagnpfozuwejmkrbvx", "qysetiklcagnpfozuwejmhrxvh",
    "qysdtiklcavnpfuzuwejmhrbvh", "qmndtiklcagnpfojuwejmhrbvx", "qysdtialcagnpfozuwejmdrqvx", "qysdtiklcagnpfozuwejtzrbvv",
    "qysdtiklxagnpyozufejmhrbvx", "qysdtiklcagnpfgzewejahrbvx", "qysdtiklcagppsozuwejmhrdvx", "qykdtiklcainpfozuwejqhrbvx",
    "qysdtiklcagnpfszxwejmhubvx", "qyrdtiklcagkptozuwejmhrbvx", "qysdsiklcagnpfozsvejmhrbvx", "qypdtiklcagypfozuwejmhrlvx",
    "qssdtiklcagnpfozuwqjmirbvx", "qyshtiklcagnpfrzuwyjmhrbvx", "qysdtiklcagnpfqzuwenmgrbvx", "qysdtiklcagnpfonuwejmhkwvx",
    "qysdhiklcagnpfokuwejmhrfvx", "jysrtiklcaenpfozuwejmhrbvx", "qysdtiilcagnpfozuwejmhcbvl", "qysdtiklcagnheozuwejmhrbvn",
    "qysdtikucagwpfojuwejmhrbvx", "qysdtinlctgnpfozuwujmhrbvx", "qysdtiklcagnpiozuwejmtrbjx", "qysktiklcagqpfozuwcjmhrbvx",
    "qysddiklcagnpfozpwejmhrbvh", "wysdtiplcagnpfozuwejyhrbvx", "qysdtiklcagnpfjzlwejmhrcvx", "qysdtikleagopbozuwejmhrbvx",
    "qysdtqklcwgnpfozuwejmirbvx", "qysdtiklcugnpmozuwejmhrbvp", "qysdtiklcagnpfozpwejmnrbvz", "qysdtiklcagnpcozuwejmhbbmx",
    "uysitiklcagnpfozewejmhrbvx", "qykdtiklcasnpfozuwejdhrbvx", "qyjdtiklcagnpqozuzejmhrbvx", "qysdtiklcagaifozuwejmhrbvh",
    "qysdtiklcagnhfozuwyjrhrbvx", "qysetiklcaanpfozuwyjmhrbvx", "qyfdtiklcagnphozulejmhrbvx", "qysdtikkcrgnpfozuwejmhpbvx",
    "qysdtiklcarnpfdzuwejmhrbvq", "qysdtiklcfyrpfozuwejmhrbvx", "rysdtitlcagnpfoznwejmhrbvx", "qysdtiilcagnffozugejmhrbvx",
    "qysdyifloagnpfozuwejmhrbvx", "qysdtiklcegnpfozuwejmlrcvx", "qysdtiklcagnpfozuwajmhbbqx", "qysptrklcarnpfozuwejmhrbvx",
    "qysdtiklcagnldozuwejmhwbvx", "qysdtiklczgqpfozuwejmhobvx", "qyxdtiklcagcpfoiuwejmhrbvx", "qysatiklczgnpfozawejmhrbvx",
    "qysduiklcagnpfoziwejyhrbvx", "qysdtgklqagnpfozujejmhrbvx", "qysdtiqlcagnpfozzdejmhrbvx", "qysdtiklcngnpfofuwejmzrbvx",
    "qysdtiklcagnyfozuwejrnrbvx", "qysdtiplcagnpfozowmjmhrbvx", "qyswtiklcagnplozuwedmhrbvx", "qyseiiklcagnpfozuwejmhibvx",
    "qysdtiklcagnpfozutusmhrbvx", "qysdtimlcagnpfozccejmhrbvx", "qnsdniklcagnpfobuwejmhrbvx", "qysrtiklcagnpfofuwejmhrbyx",
    "qyzdtiklcagnpfoizwejmhrbvx", "qysdtjslcdgnpfozuwejmhrbvx", "qysdtiklcagnpxoyuwejmrrbvx", "qysdtikllagnpfmzuwbjmhrbvx",
    "qysdtitlcagnkfozuwejwhrbvx", "qymdtiklcggnpfozuwejmzrbvx", "qysdtiklclfnpfozuhejmhrbvx", "qysdtyklcagnpfozuwejmhhbix",
    "qysetiklcagnpfozuwejmhrspx", "qysdipklcagnpfozuwejmhrbex", "uysgtiklcagnpmozuwejmhrbvx", "qysdtiklmagnpfozuwqlmhrbvx",
    "qysdtiklcagnyfozxwejmhrmvx", "qysutillcagnpfozuwejmhrbbx", "casdtiklcagnpfopuwejmhrbvx", "qesdtiklctgnpfmzuwejmhrbvx",
    "qysdtiklcagopfozjwejmdrbvx", "jzsdtiklcagnpfozuwejmurbvx", "qysdtiklcjgnpfonuwejrhrbvx", "qysdtiklcrgnpnozuwejmhqbvx",
    "oyhdtiklcagnpfozuwekmhrbvx", "qysstiklcagjpfozuwejmhrbnx", "qyudtiklsagnpsozuwejmhrbvx", "qysdtiilcagnpfozusejmhrbva",
    "qysdtiklcaknpfozmwejmhgbvx", "qysdbiklcpgnpfozuwejmrrbvx", "qybdtiklcagvpfokuwejmhrbvx", "qysatiklcagnpwofuwejmhrbvx",
    "qysdtiklcadnpfonuwejmcrbvx", "qysdtijfcagnpfozuvejmhrbvx", "qysdtiklcagnpfhluuejmhrbvx", "qysdtiklcagnpfoguwejqhrwvx",
    "qlsdtiklcagnpfojuwehmhrbvx", "qyhdtiolcagnpfozuwejmhrzvx", "qmsdtiklcagnppozuwpjmhrbvx", "qysdtiklvvgnpfvzuwejmhrbvx",
    "qysdtiklcagnpfszuwajmhrcvx", "qysdtiklcagnpfmzuwekmhrbyx", "qysdtiklcagwpfozumevmhrbvx", "qysdtaklcagnpfozuwejvhzbvx",
    "qysotiklcagntffzuwejmhrbvx", "qysdtiklcagnpfowuweqmhrivx", "qysdtrkloagnxfozuwujmhrbvx", "qasdiiklcagnpfozuwegmhrbvx",
    "qysbtiklcagnpfozuwejthrbhx", "hysdtikllagnpfozuwejmhrbbx", "qyqdtiklcagnpsozuwejmcrbvx", "qysdtiklcagnpiqzuwejmhrbux",
    "qnsdtiklcagnpfozdwejmhbbvx", "qysjbiklcagzpfozuwejmhrbvx", "qysdtiklcagnpfifuwejmhrbvg", "qysdtiklcaggpkozunejmhrbvx",
    "qxsdtiklcavnpfozuwfjmhrbvx", "qysdtikycabnpfkzuwejmhrbvx", "qyswtzklcagnpfozuwejmhrlvx", "qysdtikqcagnpfozuwejrhnbvx",
    "qysdtiplaagnpfozuwejmhruvx", "qjcdtiklcagnpfozujejmhrbvx", "nysdtyklcagnpfozutejmhrbvx", "qysrtiklcagnpfnzuwejmhrbdx",
    "zysdtielcagnpfozuwezmhrbvx", "qysdtikpvagnpfozuzejmhrbvx", "qysdwiklcagnpfozueejmhrlvx", "dysdmiklcagnpfozuwejzhrbvx",
    "qysdtiklcjgnpfozuweimhmbvx", "qysdtiklciynpyozuwejmhrbvx", "qksdtiklcagnpbozubejmhrbvx", "qysdtiklkagnpfozuwejmhrjvb",
    "yyxdtiklcagnpfomuwejmhrbvx", "qysdtiklcagnfnozuwejmhrbvv", "qysdtzklcagnpfozuwejmhrmvb", "qysduiklclgnpfozuwejmhrbvn",
    "qyndtmklcavnpfozuwejmhrbvx", "qisdkiklcagnpfozuwqjmhrbvx", "qysdtrkycagypfozuwejmhrbvx", "qhsdtiklcwgnmfozuwejmhrbvx",
    "qysdaiklcannpfozupejmhrbvx", "zysdtiklcagnpjozuwejmhrbwx", "qysdtikxcagnpfozuwejmcrxvx", "qysdtzklcagnpfozewejmhrbvk",
    "qysdwtklcagnhfozuwejmhrbvx", "qysdtqklcaenpfozuwejmdrbvx", "qysdtiklcagnpfozuoeemhqbvx", "nysdtikocagnpfozuwejmhwbvx",
    "qysxtiklcagnpfozqwejmhrbax", "qysdtielcasnpfozuwejmhsbvx", "qysdtiklcaknpfozuwejcwrbvx", "qysytiklcagnpfozdfejmhrbvx",
    "qysdtiklcagmpfozuwejmgrbox", "qysdtielcagnpfpzuwejhhrbvx"
];

nTwoUnique = 0;
nThreeUnique = 0;

for id in listOfIds:
    uniqueChars = {};

    for char in id[::]:
        if char in uniqueChars:
            uniqueChars[char] += 1;
        else:
            uniqueChars[char] = 1;

    hasUniqueTwo = False;
    hasUniqueThree = False;

    for key, value in uniqueChars.items():
        if value == 2 and hasUniqueTwo is False:
            nTwoUnique += 1;
            hasUniqueTwo = True;
        if value == 3 and hasUniqueThree is False:
            nThreeUnique += 1;
            hasUniqueThree = True;

print(str(nTwoUnique * nThreeUnique));