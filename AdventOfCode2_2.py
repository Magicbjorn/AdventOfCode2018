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

correctIds = [];

length = len(listOfIds) - 1;

for index in range(0, length):
    string_1 = listOfIds[index];

    index_2 = 0;

    for string_2 in listOfIds:
        print(string_1 + " and " + string_2, end=" : ");

        if index_2 is not index:
            nAmountTheSame = 0;
            for i in range(len(string_1)):
                if string_1[i] == string_2[i]:
                    nAmountTheSame += 1;
            print(len(string_1) - nAmountTheSame);
            if len(string_1) - nAmountTheSame is 1:
                if [string_1, string_2] not in correctIds and [string_2, string_1] not in correctIds:
                    correctIds.append([string_1, string_2]);
        else:
            print('n/a');
        index_2 += 1;

correct_string_1 = correctIds[0][0];
correct_string_2 = correctIds[0][1];

correct_string = "";

for i in range(len(correct_string_1)):
    if correct_string_1[i] != correct_string_2[i]:
        print(correct_string_1[i] + " and " + correct_string_2[i]);
        correct_string = correct_string_1[:i] + correct_string_1[i + 1:]

print(correctIds);
print(correct_string);