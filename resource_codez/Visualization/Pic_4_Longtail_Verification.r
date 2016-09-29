data = read.csv("C:\\Users\\XiaoX\\Desktop\\Project _科学合作与科学影响力\\Work_统计分析_Statistical_Analysis_20151119\\LongtailVeri_20151216.csv")
x <- 1:79
Dsharers <- data[1:79,2]
Idsharers <- data[1:79,1]

plot(x,Dsharers)
fit <- nls(Dsharers ~ a*x^b)
lines(seq(1, 79, by = 0.1), predict(fit, data.frame(x=seq(1, 79, by = 0.1))))
summary(fit)

plot(x,Idsharers)
fit <- nls(Idsharers ~ a*x^b)
lines(seq(1, 79, by = 0.1), predict(fit, data.frame(x=seq(1, 79, by = 0.1))))
summary(fit)

Temp_Ds = Dsharers + 4
plot(x,Temp_Ds)
fit <- nls(Temp_Ds ~ a*x^b)
fit