import time
from threading import Timer

time_start = time.time()

def fun_timer():
    time_now = time.time()
    print("running, time cost: ", time_now-time_start, "s")

Timer(0, fun_timer).start()


def open_small_library(text_name):
    text_path = text_name + ".txt"  # 尽量不要拼接txt, 直接读取文件名
    file = open(text_path, "r")
    gene_list = [x.strip("\n") for x in file]
    file.close()
    # print(text_path, "\n",gene_list[:10],"\n", gene_list[-10:], "\nlength: ", len(gene_list))

    return gene_list


# open_small_library("3-HKG(841).txt")


import pandas as pd 

total_gene_df = pd.read_excel("whole-genome_sgRNA_library.xlsx", usecols= [0, 1, 2, 3, 4, 5, 6, 7])

# total_gene = total_gene_df.drop_duplicates(['Gene'])
# total_gene_set = total_gene['Gene'].tolist()

# http://www.cppcns.com/jiaoben/python/230972.html
# https://www.cnblogs.com/Jomini/p/8636129.html


import os 
now_path = os.getcwd()
# print("\nnow path:", now_path)
txt_path_work = now_path + "/*.txt"

from glob import glob  # glob模块用来查找文件目录和文件

total_txt = glob(txt_path_work)
total_txt_list = [i.split(now_path + "\\")[-1].split(".txt")[0] for i in total_txt]

# print(total_txt_list)


# total_df = total_gene_df.drop(total_gene_df.index, inplace= True) change raw df
# total_df_index = total_gene_df.drop(total_gene_df.index) 注意函数修改原始dataframe

small_library_merge_sgRNA =pd.DataFrame(columns= total_gene_df.columns.values)

# a_small_library_df = total_df_index.drop(axis=1, )
# a_small_library_df = pd.DataFrame()

for text_name in total_txt_list:
# for  text_name in ["4-OTHERS(205)", "4-RBP-ONLY(30)", "4-TF-COTF(48)"]:
    a_small_library_df = pd.DataFrame(columns= total_gene_df.columns.values)
    # a_small_library_df["pubmed_website"] = ""
    for gene in open_small_library(text_name):
        try:
            # print(total_gene_df[total_gene_df["Gene"] == gene])
            # gene in total_gene_set
            # print("\n", gene)
            total_gene_df.loc[total_gene_df["Gene"] == gene]
            # print(type(total_gene_df.loc[total_gene_df["Gene"] == gene]))
        except IndexError:
            print("gene donnot exist: ", gene)
        else:
            add_sg_df = total_gene_df.loc[total_gene_df["Gene"] == gene]
            # add_sg_df["pubmed_website"] = "https://www.ncbi.nlm.nih.gov/pubmed/?term=" + gene
            a_small_library_df = pd.concat([a_small_library_df, add_sg_df], axis=0)
            # a_small_library_df.append(total_gene_df.loc[total_gene_df["Gene"] == gene])

        
    # csv_name = text_name + ".csv"
    # a_small_library_df.to_csv(csv_name)
    excel_name = text_name + ".xlsx"
    a_small_library_df.to_excel(excel_name)

    fun_timer()

# https://blog.csdn.net/roamer314/article/details/80886075


    small_library_merge_sgRNA = pd.concat([a_small_library_df, small_library_merge_sgRNA], axis=0)

small_library_merge_sgRNA.index=range(len(small_library_merge_sgRNA["Gene"]))
# small_library_merge_sgRNA.to_csv("small_library_merge_sgRNA.csv")

True_timer = False

# print(total_df.head())

# 注意函数是否修改原始dataframe
