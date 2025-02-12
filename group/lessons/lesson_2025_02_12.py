"""Lesson 2025-02-12"""

from datetime import datetime as dt

start = dt.now()

# Не ок
# def MyFunc():
#    pass

# Ок
def my_func():
    pass

# Не ок
# myVar = 1

# Ок
my_var = 1


def factorial(n: int|float) -> int:
    """
        Считает факториал
        В случае ошибки вернем -1
    """
    
    answer = 1
    if n < 1 or int(n) != n:
        return -1
    
    for i in range(1, int(n) + 1):
        answer *= i

    return answer


print(factorial(n=5.0))


search_list: list[int] = [21442209, 51878540, 68780009, 120212804, 294524198, 364174904, 371209088, 597638180, 772407311, 824869215, 849264930, 1154001059, 1204459437, 1283242932, 1341447041, 1492306292, 1495526062, 1669154981, 1711810862, 1829637351, 1949822110, 1982513661, 1989743918, 2070190387, 2108538187, 2194932903, 2248786359, 2286048244, 2298287411, 2475581406, 2689538354, 2787102071, 2795459106, 2909017851, 3261572806, 3290559601, 3313627977, 3435182256, 3478477319, 3528962057, 3591019508, 3638514561, 3650665191, 3805940458, 4084388832, 4092055456, 4222859712, 4297723546, 4301208454, 4324586129, 4434966514, 4485972170, 4603687189, 4836702798, 4945274056, 5004629018, 5039060213, 5111534746, 5266221360, 5346919970, 5512141711, 5547887534, 5571296243, 5620435590, 5647541816, 5886620696, 5921828168, 5972008892, 6051530943, 6123531316, 6177432140, 6377290546, 6739262456, 6843070449, 6867040124, 6917546096, 6974764544, 6985369741, 7072121179, 7161875989, 7307205455, 7372893219, 7443545301, 7515087138, 7620517021, 7820405179, 7860126701, 7930116743, 8218332050, 8241549888, 8293214486, 8594935293, 8623841927, 8675382478, 8677895411, 8683455798, 8874689337, 8906930305, 8972510352, 9019106317, 9087948598, 9088629680, 9193454434, 9219429104, 9233723211, 9479531447, 9511033856, 9864049756, 10169316318, 10231514388, 10251943422, 10537486681, 10644093513, 10673877644, 10714068172, 10745237293, 10768542863, 10911594938, 10977234940, 11046637197, 11127003626, 11219038341, 11473496025, 11533222444, 11602447734, 11622404939, 11987009931, 12023161378, 12047867659, 12112602654, 12171668130, 12436381166, 12439890519, 12683859342, 12745965708, 12817935790, 12974582422, 12998948631, 13127098079, 13357438491, 13775206031, 13826403621, 13839064021, 13845338324, 13927727787, 13949383139, 14011524781, 14126035426, 14161715992, 14169308926, 14173472711, 14230420487, 14256639680, 14365361018, 14440426447, 14883841067, 14901210716, 14952473335, 15006527328, 15600855893, 15601821002, 15656909319, 15690065617, 15744804424, 15787196547, 15825487432, 15940175411, 16011634678, 16105662412, 16303037755, 16444712767, 16481503089, 16501305566, 16585997882, 16594344241, 16618816446, 16636084002, 16671974781, 16793649220, 16990793637, 17087337985, 17380170140, 17454649135, 17560941219, 17602721921, 17624721659, 17662211154, 17896100233, 17924093067, 17953901684, 18088514307, 18148552917, 18205798476, 18293675711, 18296065079, 18398713057, 18420701481, 18439790480, 18668320465, 18706464398, 18815032074, 18827130276, 18840985982, 18920622169, 19044555315, 19290405022, 19335273485, 19507317033, 19632021257, 19672529122, 19772964593, 19837191415, 19946195845, 20128689391, 20180027844, 20198104069, 20249528889, 20519692458, 20576075987, 20615574729, 20621140174, 20645832148, 20693059377, 20767843177, 21003898814, 21007512696, 21061262823, 21064163116, 21289474859, 21385462288, 21498311288, 21553211159, 21893578950, 22115738321, 22282327293, 22320898457, 22348849599, 22381722536, 22503017185, 22587200929, 22667470058, 22677526193, 22766354853, 22811552484, 22864208238, 23085987613, 23126193865, 23320600476, 23343749868, 23463721338, 23521545074, 23827090037, 23868407055, 23906664447, 23922534831, 23937370663, 23998343909, 24096049627, 24147311694, 24401353835, 24451127814, 24457260430, 24502636932, 24512365429, 24518195806, 24566773470, 24684287132, 24694113530, 24749643389, 25169648945, 25364776466, 25427665399, 25509534487, 25652257693, 25738880365, 25797887790, 25947234977, 25950799527, 26314438758, 26551506807, 26582047737, 26760602257, 26826740740, 26900492872, 27012167664, 27023669605, 27211317507, 27258188695, 27334874471, 27683409422, 27872207691, 27902748954, 27990756528, 28092923654, 28251848843, 28366184934, 28408432307, 28492217424, 28584057761, 28593621963, 28638229703, 28951888138, 28988968116, 29221316295, 29277079548, 29305680016, 29611476109, 29620982904, 29912930487, 29914592990, 29925115006, 29942474818, 30056002256, 30912705243, 30980008723, 31011986226, 31094180545, 31148451516, 31297788340, 31306087163, 31506019467, 31507020197, 31600098936, 31713435699, 31834072957, 31870562378, 31924239341, 31958041596, 32263462188, 32295265817, 32298456884, 32341650375, 32423984300, 32509939511, 32526603877, 32543473741, 32605827332, 32666549759, 32690130535, 32878599114, 32983639145, 33078998941, 33095845235, 33099546432, 33254804392, 33305198670, 33329658476, 33351681419, 33445905158, 33597281019, 33617531194, 33733524645, 33770855715, 33808024282, 33835518872, 33864395868, 33959926164, 34095142261, 34291113282, 34307167580, 34411432176, 34470029310, 34667801794, 35138926156, 35388223744, 35494319491, 35503330374, 35522731265, 35579602206, 35788168445, 35908312860, 36066264500, 36083873948, 36110144023, 36217375939, 36357279803, 36417323959, 36499269263, 36550946397, 36612508870, 36736261141, 36947126178, 37174291652, 37198163339, 37229834698, 37293229740, 37388994811, 37407952642, 37428582901, 37518830639, 37731358100, 37787992064, 38133926023, 38152320421, 38248378586, 38249462207, 38385719073, 38430153420, 38467569463, 38766024138, 38789909191, 38850995024, 38932526256, 38994668999, 39061967451, 39064010580, 39342649083, 39525418120, 39714505680, 39754576627, 39763858689, 39834621724, 39848507934, 39928463646, 40087532415, 40174256309, 40342986738, 40388295049, 40571657992, 40581674275, 40680254506, 40799410351, 40822060401, 40824398685, 40830561790, 41077424469, 41102717312, 41163084673, 41177522884, 41234209341, 41276940611, 41396396882, 41406562994, 41530606960, 41641398482, 41702683336, 41710786006, 41715986179, 41743291138, 41861316181, 42014586781, 42078001582, 42102053364, 42199986367, 42336898562, 42370788890, 42489697326, 42523648725, 42531410073, 42635891236, 42910677125, 42940081027, 43001600809, 43081734609, 43086542490, 43096118997, 43214007324, 43263324341, 43264759938, 43272757425, 43277571088, 43297203594, 43308974521, 43412120783, 43648548276, 43661535306, 43670372239, 43731755593, 43777827647, 43781516771, 43782548435, 43799014380, 43841694893, 43846715961, 43910742824, 44201056481, 44344680188, 44443674263, 44605342229, 44699940064, 44754160567, 44870348603, 44934351580, 45110689790, 45202623320, 45372242213, 45405108065, 45406388556, 45526548282, 45677795551, 45741462754, 46007086372, 46241036525, 46291647863, 46297913511, 46330527327, 46392474417, 46573738056, 46622412246, 46689168184, 46811756328, 46898126643, 47009616446, 47160516488, 47494908574, 47629272365, 47687232412, 47928392630, 47958384526, 47979645329, 48034378940, 48285513702, 48449206388, 48522667116, 48675030894, 48706649997, 48751484895, 48968255666, 49125666478, 49219077593, 49513732698, 49561896200, 49569939073, 49633802479, 49659647796, 49710423311, 49751632373, 50019178270, 50182605616, 50263834048, 50298201435, 50537775945, 50617050804, 50631594579, 50706047781, 50727735403, 50814159573, 50819865363, 50853790519, 50943364752, 51085913784, 51108678100, 51139619337, 51170934337, 51382682995, 51405284126, 51435960096, 51653609619, 51939350654, 52014759233, 52068168487, 52111500050, 52229777947, 52341241562, 52545118881, 52585635667, 52676233714, 52686905740, 52701092508, 52714091449, 52743697745, 52793082981, 52878335503, 52970186230, 52984420680, 53007579155, 53056500381, 53089884127, 53146902471, 53334272660, 53517010518, 54096650285, 54193620264, 54216675198, 54392752460, 54451125775, 54541999196, 54549621367, 54686810077, 54751649476, 55005057868, 55060082798, 55099241751, 55514060020, 55633268154, 55705325635, 55769414721, 55960351009, 55977853090, 55998592707, 55999607575, 56088247865, 56213198321, 56269639591, 56341657208, 56401803311, 56413612129, 56617604104, 56812457614, 56908438633, 56909813592, 56915701648, 57067439168, 57131968322, 57234938537, 57305840605, 57354483413, 57397105204, 57465854113, 57473249179, 57520974813, 57938386776, 57949054483, 58125411665, 58139305379, 58185135933, 58321561210, 58381198241, 58394466903, 58395284159, 58650146528, 58927846624, 58966527426, 59057563134, 59095532951, 59547422317, 59558466385, 59772463655, 59875595140, 59956468779, 60181109321, 60316408165, 60457633954, 60495116933, 60627107280, 60682975632, 60701872661, 60738855933, 60791910958, 60897089899, 60980190889, 61065302289, 61184943395, 61475635729, 61678282548, 61743413710, 61863332136, 61917058162, 61947112375, 61972368980, 62134049467, 62163095880, 62173582723, 62174476525, 62299836895, 62306514242, 62604719491, 62737163398, 62831215617, 62884923110, 62905743385, 63078402351, 63083150938, 63197416001, 63220821933, 63322475822, 63350197530, 63362284099, 63371624841, 63538092562, 63578926731, 63697943696, 63825992547, 64122381319, 64252475802, 64376054049, 64435706692, 64610392491, 64760884421, 64843809937, 64917415060, 65499374038, 65593410516, 65612790865, 65642789389, 65663252140, 65834197370, 66276811286, 66514210674, 66752133522, 67003803376, 67245728506, 67261954511, 67276010682, 67323509728, 67585869608, 67747653423, 68080192069, 68147251235, 68160096583, 68173034755, 68194326134, 68220846370, 68295507760, 68391334184, 68503794017, 68703244724, 68817959452, 68973008822, 69127915085, 69267760395, 69333954630, 69735631781, 69736493693, 69828405463, 69856098873, 69857094991, 69866893091, 69893706998, 69947146113, 70028826821, 70195043843, 70284237049, 70502308956, 70657880967, 70684644847, 70771302822, 70842987930, 70876111681, 70936714377, 70957123527, 71140150796, 71317983243, 71397978321, 71401661899, 71419833235, 71455195140, 71541343482, 71837139082, 72173840373, 72193936307, 72231928559, 72422837550, 72455467539, 72597757917, 72882222874, 73030592476, 73521892985, 73766798102, 73856108793, 74070994810, 74228177951, 74263020891, 74279703472, 74331410726, 74427947589, 74543714779, 74557910669, 74585142174, 74745327005, 74830442643, 74888064273, 75144145078, 75368195268, 75411116592, 75608312139, 75707143569, 75747446551, 75749806529, 75841961513, 75937717294, 76008605465, 76047737651, 76092150261, 76194425571, 76324369545, 76411693008, 76617789150, 76687836333, 76690983181, 76854015600, 76987578216, 77005390062, 77051199854, 77221133404, 77241183760, 77243076751, 77271775063, 77743692703, 77805890615, 77867628905, 77878690716, 78107322071, 78181644568, 78373296823, 78549442662, 78633665303, 78651241749, 79017348109, 79183582035, 79676154767, 79825971487, 79971150612, 80164405135, 80215643234, 80285852435, 80378909525, 80564069096, 80567920336, 80681237353, 80689782503, 80863543273, 81169024196, 81245685986, 81389997541, 81696462900, 81797232146, 81828713911, 81839582177, 81911981194, 81976948689, 81977932134, 82171494953, 82194948496, 82209092434, 82309297237, 82342799710, 82352751240, 82416845528, 82482380200, 82508004283, 82557186160, 82592398751, 82774487116, 82810530416, 82928750553, 83134194966, 83137845439, 83164767851, 83187169283, 83408146792, 83524825599, 83629997929, 83661218620, 83746900858, 83774910438, 83826137283, 83998824988, 84130696735, 84296181246, 84440110188, 84576144397, 84610293920, 84640133650, 84645433634, 84686383574, 84713055402, 84853287006, 84871228474, 84985620441, 85044206772, 85171453831, 85236519528, 85497035717, 85635301246, 85655142965, 85740369449, 85907635511, 85915897363, 85931914020, 85980672870, 86002959799, 86153340638, 86202036356, 86317712243, 86371806430, 86481215854, 86530037029, 86530682998, 86534904796, 86537378964, 86689834934, 86812528934, 87237362222, 87271335237, 87337361775, 87484405972, 87571374625, 87612330714, 87636370309, 87647538128, 87768575529, 87778626851, 87828124188, 87956893696, 87973174583, 87984728430, 88334331900, 88575719731, 88830318383, 88958011970, 89038729699, 89150988873, 89159206307, 89181609389, 89208621441, 89221396267, 89331225695, 89416904404, 89594106450, 89777289346, 89902931868, 89905326922, 90127947801, 90382633067, 90473554759, 90622411347, 90737628333, 90784273833, 90998212714, 91035059837, 91038542511, 91093232362, 91211418489, 91257860341, 91313493202, 91317532257, 91692402151, 91749601723, 91886933917, 92043894829, 92078316635, 92237486304, 92287890630, 92288561204, 92588974062, 92855799377, 92895877606, 92943547633, 93110503077, 93303883118, 93432178349, 93503356655, 93506694071, 93589999063, 93806325707, 93823098686, 93978371638, 94063996470, 94077990755, 94556077499, 94557495991, 94570831099, 94750302683, 94782556107, 95003146802, 95180568012, 95340383538, 95441486147, 95623359455, 95637434836, 95654305349, 95696889808, 95863089186, 95886017627, 95900745187, 96150778425, 96260671072, 96514925093, 96635710223, 96664714416, 96782251515, 96795532831, 96812352739, 96828259031, 96970884660, 97075840126, 97203871849, 97561001178, 97583252815, 97651348552, 97722516134, 97768644782, 97902516400, 98055142829, 98055387242, 98087492296, 98188702637, 98242389001, 98288620831, 98460381888, 98794203929, 98844822964, 99070423304, 99228155313, 99240127140, 99443079364, 99755441681, 99802529456, 99968368638]

count: int = 0

def binary_search(nums: list[int|float], search_num: int|float) -> bool:
    """Бинарный поиск"""

    length_nums: int = len(nums)
    left_list: list[int|float] = nums[:int(length_nums/2)]
    right_list: list[int|float] = nums[int(length_nums/2):]
    
    global count
    count += 1

    if len(left_list) > 0 and search_num >= left_list[0] and search_num <= left_list[-1]:
        if len(left_list) == 1 and left_list[0] == search_num:
            return True
        elif len(left_list) == 1:
            return False
        else:
            return binary_search(left_list, search_num)

    elif len(right_list) > 0 and search_num >= right_list[0] and search_num <= right_list[-1]:
        if len(right_list) == 1 and right_list[0] == search_num:
            return True
        elif len(right_list) == 1:
            return False
        else:
            return binary_search(right_list, search_num)

    return False


print(binary_search(search_list, 51939350654))
print(count)

print(dt.now() - start)
