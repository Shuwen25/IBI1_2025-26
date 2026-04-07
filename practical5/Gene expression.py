Gene_expression={"TP53":12.4, "EGFR":15.1, "BRCA1":8.2, "PTEN":5.3, "ESR1":10.7}
Gene_expression["MYC"]=11.6

import matplotlib.pyplot as plt
import numpy as np

N=6
gene = list(Gene_expression.keys())
expression = list(Gene_expression.values())
width= 0.35

p1=plt.bar(gene,expression,width)
plt.ylabel("Expression Level")
plt.xlabel("Gene Name")
plt.title("Expression Values of All Genes")
plt.yticks(np.arange(0,20,5))
plt.xticks(rotation=15)
plt.show()

Gene_of_intrest=("TP53") #input specific gene name
if Gene_of_intrest in Gene_expression:
    expression_value=Gene_expression[Gene_of_intrest]
    print(f"The expression of gene {Gene_of_intrest} is {expression_value}")
else:
    print("error.The gene is not in the Gene_expression dcitionary.")

average=sum(expression)/len(expression)
print(f"average	gene expression:{average}") 