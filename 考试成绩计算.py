# 输入试卷满分及扣分区域数量信息
x = int(input("请输入总题数（记分区域总数）："))
Total_Part = list(range(1,x+1))
All = float(input("请输入卷面总分："))
origin_All=All
All_stu = ()
# 保证无需重复运行代码的情况下多次输入学生分数计算
while True:
    try:
        name = input("请输入姓名/学号：")
        error = 0
        # 输入学生姓名学号后，开始按题号依次输入扣分
        for i in Total_Part:
            kf = float(input("请输入第" + str(i) + "部分扣分(正值，单次不大于20分)："))
            # 卷面单题扣分一般不大于20分，可以简单排查出输入错误，并能够重新输入分数
            if kf >= 20:
                error = error + 1
                continue
            All = All - kf
        if error >= 1:
            elist = list(range(1, error + 1))
            for j in elist:
                kf = float(input("请修正第" + str(j) + "次错误输入："))
                All = All - kf
        # 计算得分并显示最终成绩
        print("总成绩是：" + str(All))
        # 记录多个学生成绩
        new_stu = (name, All)
        All_stu = All_stu + new_stu
        # 将计算起始点归位到卷面总分
        All=origin_All
        # 退出后显示全部学生学号/姓名及成绩
        tc = input("你是否想退出：")
        if tc == "是":
            print(All_stu)
            break
    # 排除输入错误
    except TypeError:
        print("输入错误")
    except ValueError:
        print("输入错误")
