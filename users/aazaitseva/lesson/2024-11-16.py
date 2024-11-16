one_inc = lambda x, y: (x+1, y-1)
print(one_inc(1, 6))

def factorial(num: int) -> int:
    answer = 1
    if num < 1:
        return 0
    while num > 1:
        answer *= num
        num -= 1
    return answer
print(factorial(5))

[5, 4]
#print(n)

[1, 5]

var_list = [2009, 3604, 5203, 5656, 6765, 7494, 10719, 12222, 13590, 13976, 14279, 15391, 15537, 23531, 23873, 23901, 25179, 32324, 35120, 36225, 39093, 40791, 44993, 46327, 47151, 47545, 52347, 53504, 53695, 58180, 60274, 62117, 62194, 66201, 67619, 68839, 69415, 69810, 71241, 71276, 72842,
76221, 78165, 78758, 79151, 81101, 82341, 83926, 85073, 85906, 92735, 93140, 95348, 96785, 96999, 99131, 100245, 102453, 103954, 104770, 107418, 110756, 111588, 112990, 115461, 118237, 126297, 126790, 128380, 129628, 131562, 132897, 133118, 138891, 141518, 143598, 143659, 143775, 149751, 149903, 150183, 152143, 155804, 159168, 159181, 159847, 168017, 169399, 171919, 173981, 175819, 178500, 181920, 191114, 191280, 192083, 194807, 197235, 197884, 200554, 201795, 203045, 214113, 218144, 225290, 229627, 230604, 231359, 231811, 233778, 236094, 236226, 236491, 238010, 239644, 240164, 241056, 241286, 245010, 247168, 247801, 248667, 250366, 250723, 252461, 254324, 258634, 260072, 263516, 264918, 268092,
268097, 269891, 271599, 279114, 284839, 295869, 296490, 299076, 299514, 300245, 300301, 300329, 301250, 302150, 304430, 308147, 309586, 310629, 310633, 313982, 315699, 316220, 317190, 318188, 322353, 323896, 328272, 329012, 333548, 335094, 335970, 336059, 336535, 338179, 341366, 341844, 346754, 351122, 351171, 353196, 365752, 370407, 372813, 372814, 373195, 374145, 378776, 378983, 381988, 382172, 383235, 383744, 384120, 385775, 386174, 388671, 389328, 390924, 392515, 402330, 404829, 407773, 409040, 410203, 414835, 416260, 416808, 418090, 421062, 421260, 422049, 423391, 423842, 424342, 427265, 429965, 430162, 432097, 434188, 434451, 435223, 435336, 435943, 439626, 445118, 446597, 447545, 448403, 449232, 451037, 453249, 454184, 456391, 456921, 459933, 460036, 460597, 462634, 464965, 465654, 466392, 467061, 474370, 477254, 478113, 478857, 481028, 484476, 486470, 488097, 490991, 492934, 494938, 495472, 495986, 503807, 505099, 505182, 505816, 505906, 506226, 507020, 510732, 510783, 511070, 514286, 514809, 515050, 518933, 520341, 521578, 523664, 529551, 531455, 533083, 535165, 536326, 537174, 540609, 548438, 549004,
549408, 553497, 557811, 558969, 559775, 560965, 561539, 561903, 563763, 563856, 564710, 565365, 572916, 574252, 575483, 579061, 583380, 583841, 584736, 589606, 591516, 592093, 592995, 594532, 598245, 600389, 600576, 602013, 604642, 607252, 607266, 607426, 617207, 620820, 621546, 622760, 623495, 628768, 629060, 630016, 630123, 630481, 634082, 639976, 640644, 642337, 642340, 643472, 643704, 643745, 645334, 645455, 648291, 651764, 652784, 654070, 659869, 661308, 664174, 668399, 668550, 677990, 679124, 681243, 685006, 687731, 688631, 689768, 690273, 690687, 691266, 691770, 693531, 694920, 695452, 696841, 697207, 697448, 698637, 699169, 699888, 700450, 701553, 703877, 704273, 705223, 705414, 706618, 710650, 713463, 714210, 714633, 715250, 716913, 717522, 719319, 720457, 720572, 721658, 725709, 726636, 728307, 730325, 730724, 733154, 735480, 737596, 737998, 740077, 740856, 742867, 748529, 749380, 749858, 750064, 751930, 753865, 756337, 758395, 759901, 760332, 760510, 768928, 769310, 770355, 770516, 783982, 784000, 785323, 786601, 789741, 793452, 794533, 796972, 800295, 800914, 801343, 801873, 802403, 803685, 804059,
804234, 806087, 806711, 811895, 814251, 814326, 819018, 822456, 823163, 825788, 828888, 829925, 831582, 836547, 840775, 856424, 859933, 861452, 862250, 863371, 869843, 870609, 872396, 877869, 878200, 880728, 882026, 882972, 884739, 886595, 891236, 891934, 893193, 895757, 898768, 898943, 900501, 905752, 910672, 917844, 920177, 924757, 925464, 926984, 927154, 927260, 928075, 928704, 931117, 932909, 934538, 935365, 935815, 937643, 938946, 941205, 943142, 944448, 951431, 952790, 953338, 957698, 958048, 958439, 963424, 964887, 973127, 973221, 973894, 974852, 975194, 977852, 977902, 981654, 982651, 983249, 985255, 986658, 989062, 990219, 990607, 991317, 992529, 996009, 997231, 998433, 999329]
var_list[5]
print(var_list[5])
inc = 0
def num_in_list(num: int, serch_list: list[int]) -> bool:
    global inc 
    inc += 1
    len_list = len(serch_list)
    if len_list == 0:
        return False
    if len_list == 1 and serch_list[0] != num:
        return False
    if len_list == 1 and serch_list[0] == num:
        return True
    if serch_list[0] > num:
        return False
    if serch_list[-1] < num:
        return False
    left_list = serch_list[:len_list//2]
    right_list = serch_list[len_list//2:]
    if left_list[-1] >= num:
        return num_in_list(num, left_list)
    else:
        return num_in_list(num, right_list)
print(num_in_list(81101, var_list))
print(inc)


    
    
    