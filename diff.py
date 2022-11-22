
original = "The normality of the data is an important condition for further statistical analysis. The central limit " \
           "theorem dictates that the sample data will be approximately normal when the sample size is large " \
           "(Navidi, 2021). Although only a rule of thumb, a sample size (n) greater than 30 would constitute a " \
           "sufficiently large sample size in this case (Navidi, 2021). As our dataset contains only 37 observations " \
           "this condition is narrowly met and thus it is recommended to confirm the normality of the data. The " \
           "graphical interpretation shown in figure 2, which plots a standard normal probability against the " \
           "distribution of our error terms, suggest a roughly normal distribution (University of Utah, 2022). " \
           "Nonetheless a more robust check is desirable. This is available in the form of the Shapiro Wilk test, " \
           "which sets the null hypothesis that the data follows a normal distribution and is suitable for our sample" \
           " size (Yazici and Yolocan, 2021). The p-value of 0.087 generated by the test is greater than our critical " \
           "value of 0.05, meaning that we fail to reject the null hypothesis and our data can be treated as normal. "

new = "The normality of the data is an important condition for further statistical analysis. The central limit theorem " \
      "dictates that the sample data will be approximately normal when the sample size is large (Navidi, 2021). " \
      "Although only a rule of thumb, a sample size (n) greater than 30 would constitute a sufficiently large sample " \
      "size in this case (Navidi, 2021). As our dataset contains only 37 observations this condition is narrowly met " \
      "and thus it is recommended to confirm the normality of the data. The graphical interpretation shown in figure " \
      "2, which plots a standard normal probability against the distribution of our error terms, suggest a roughly " \
      "normal distribution (University of Utah, 2022). Nonetheless a more robust check is desirable. This is " \
      "available in the form of the Shapiro Wilk test, which sets the null hypothesis that the data follows a normal" \
      " distribution and is suitable for our sample size (Yazici and Yolocan, 2021). The p-value of 0.087 generated " \
      "by the test is greater than the critical value of 0.05, meaning that we fail to reject the null hypothesis at " \
      "5% and our data can be treated as normal. "

l1 = original.split()
l2 = new.split()

for word in l2:
    if word not in l1:
        print(word)

for word in l1:
    if word not in l2:
        print(word)