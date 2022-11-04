# oneRepMax formula:- Weight x reps x 0.0333 + weight = estimated 1RM.
modRepWeight = int(input("Please input lifting weight according to your moderate rep range:-\n(for example:- 8 reps with 20 kgs)\n"))
repRange = int(input("Please input your rep range with respect to the latter weight input:-\n"))
estOneRepMax = ((modRepWeight*repRange*0.0333) + modRepWeight)
print("Your estimated 1RPM:-\n",estOneRepMax)
