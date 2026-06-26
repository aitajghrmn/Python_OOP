def args_goster(*args):
    # args bura gələn bütün dağınıq ədədləri bir yerə yığdı.
    # Gəl onun tipini və özünü çap edib gözümüzlə görək:
    print("args-ın tipi:", type(args))
    print("args-ın içi:", args)

# Funksiyanı sadəcə ədədlərlə çağırırıq (bax, ad= filan yazmırıq!)
args_goster(10, 20, 30, 40)