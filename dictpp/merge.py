import json
import os

def dual_merge(dic1, dic2):

    tags1 = list(dic1)
    for tag in tags1:
        if(isinstance(dic1[tag],dict)) :
            if tag in dic2:
                if (isinstance(dic2[tag],dict)):
                    dic2[tag] =  dual_merge(dic1[tag], dic2[tag])
                else :
                    dic2[tag] =  dic2[tag] =  dic1[tag]
            else : dic2[tag] =  dic1[tag]
        else :
            if tag in dic2:
                if (not isinstance(dic2[tag],dict)):
                    if(not (dic1[tag] == dic2[tag])):
                        dic2[tag] = [dic1[tag],dic2[tag]]
            else : dic2[tag] =  dic1[tag]
             
    return dic2

def multi_merge(*dics):
    final_dic = dics[0]
    for i in range (1,len(dics)):
        final_dic = dual_merge(final_dic,dics[i])
    return final_dic

if __name__ == "__main__":
    pass
    dictionary =  open ('dictionary.json', 'w')

    dic2 = {"Given" : {"I" : {"login" : {"into" : {"Activeworkspace" : {"END" : "Given I login into Activeworkspace"}}}}}}
    dic1 = {"Given" : {"I" : {"click" : {"on" : {"login" : {"button" : { "END" : " Given I click on login button"}}}}}}}
    dic3 = {"Given" : {"I" : {"am" : {"connected" : {"to" : {"active" : {"workspace" : {"END" : "Given I am connected to active workspace"}}}}}}}}
    dic4 = {"Given" : {"I" : {"am" : {"gay" : {"END" : "Given I am gay"}}}}}
    
    dic5 = dual_merge(dic1,dic2)
    dic6 = dual_merge(dic3,dic4)
    dic7 = dual_merge(dic5,dic6)

    dic8 = multi_merge(dic1,dic2,dic3,dic4)

    print(dic8["Given"]["I"]["am"]["connected" ]["to"]["active"]["workspace"]["END"])
    json.dump(dic8, dictionary, indent=4)
    # print(dic5["Given"]["I"]["am"]["connected"]["to"]["active"]["workspace"]["END"])
    
    # text = json.load(dictionary)




