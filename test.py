while True:
    print("\t==========================\n"
          "\KİŞİ DEFTERİ UYGULAMASI\n"
          "\t==========================\n".center(15))
    kişi_defteri = {"ahmet" : {"memleket" : "adana",
                                 "yaş"      : "19",
                                 "meslek"   : "mühendis"},
                    "mehmet": {"memleket": "bursa",
                                  "yaş"     : "21",
                                  "meslek"  : "kantinci"},
                    "ali"   : {"memleket": "sakarya",
                                  "yaş"     : "42",
                                  "meslek"  : "programci"}
                    }
    kişi = input("kişinin ismi : ")
    if kişi in kişi_defteri:
        istek = input("bilmek istediğiniz ayrıntıları giriniz(memleket/yaş/meslek)")
        if istek in kişi_defteri[kişi]:
            print("{} adli kişinin {}i = {}".format(kişi,istek,kişi_defteri[kişi][istek]))
        else:
            print("böyle bir istekte bulunamasınız...")
    else:
        print("boyle bir kişi bulunamadı")


