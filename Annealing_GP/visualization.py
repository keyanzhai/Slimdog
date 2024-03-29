import json
import numpy as np
import matplotlib.pyplot as plt  

# def plot_figure(filename):
#     with open(filename) as json_file:
#         json_list = []
#         for each in json_file.readlines():
#             json_data = json.loads(each)
#             json_list.append(json_data)

#         y = []
#         for each in json_list:
#             y.append(each['target'])






def main():
    with open('func_test/Continuous/Continuous_2020-10-20 11:29:15.json', 'r') as json_file1: # Continuous
    # with open('func_test/AGP/AGP_S2_2020-10-19 14:41:34.json', 'r') as json_file1: # Continuous
        with open('func_test/Discrete/Discrete_S3_2020-10-20 14:28:57.json', 'r') as json_file2: # Discrete_S5
            with open('func_test/AGP/AGP_40iter_2020-10-20 14:25:01.json', 'r') as json_file3: # AGP
                # Other Discrete Settings
                # with open('func_test/Discrete/Discrete_S1_2020-10-19 13:15:58.json', 'r') as json_file4: # Discrete_S1 
                    # with open('func_test/Discrete/Discrete_S2_2020-10-18 19:53:46.json', 'r') as json_file5: # Discrete_S2
                    #     with open('func_test/Discrete/Discrete_S3_2020-10-18 19:51:01.json', 'r') as json_file6: # Discrete_S3
                    #         with open('func_test/Discrete/Discrete_S4_2020-10-18 19:47:48.json', 'r') as json_file7: # Discrete_S4

                                json_list1 = []
                                for each in json_file1.readlines():
                                    json_data = json.loads(each)
                                    json_list1.append(json_data)

                                json_list2 = []
                                for each in json_file2.readlines():
                                    json_data = json.loads(each)
                                    json_list2.append(json_data)

                                json_list3 = []
                                for each in json_file3.readlines():
                                    json_data = json.loads(each)
                                    json_list3.append(json_data)
                                
                                # json_list4 = []
                                # for each in json_file4.readlines():
                                #     json_data = json.loads(each)
                                #     json_list4.append(json_data)

                                # json_list5 = []
                                # for each in json_file5.readlines():
                                #     json_data = json.loads(each)
                                #     json_list5.append(json_data)

                                # json_list6 = []
                                # for each in json_file6.readlines():
                                #     json_data = json.loads(each)
                                #     json_list6.append(json_data)

                                # json_list7 = []
                                # for each in json_file7.readlines():
                                #     json_data = json.loads(each)
                                #     json_list7.append(json_data)

                                ## CHANGE THIS !!!
                                x = list(range(1, 104))
                                y1 = []
                                y2 = []
                                y3 = []
                                # y4 = []
                                # y5 = []
                                # y6 = []
                                # y7 = []

                                for each in json_list1:
                                    y1.append(each['target'])
                                
                                for each in json_list2:
                                    y2.append(each['target'])
                                
                                for each in json_list3:
                                    y3.append(each['target'])

                                # for each in json_list4:
                                #     y4.append(each['target'])
                                
                                # for each in json_list5:
                                #     y5.append(each['target'])
                                
                                # for each in json_list6:
                                #     y6.append(each['target'])
                                
                                # for each in json_list7:
                                #     y7.append(each['target'])
                                
                                y1 = y1[:len(x)]
                                y2 = y2[:len(x)]
                                y3 = y3[:len(x)]
                                # y4 = y4[:len(x)]
                                # y5 = y5[:len(x)]
                                # y6 = y6[:len(x)]
                                # y7 = y7[:len(x)]

                                max_indx1 = np.argmax(y1) #max value index
                                max_indx2 = np.argmax(y2) #max value index
                                max_indx3 = np.argmax(y3) #max value index
                                # max_indx4 = np.argmax(y4) #max value index
                                # max_indx5 = np.argmax(y5) #max value index
                                # max_indx6 = np.argmax(y6) #max value index
                                # max_indx7 = np.argmax(y7) #max value index

                                l1 = plt.plot(x, y1,'bo',label='Continuous', zorder = 10, alpha = 0.6)
                                plt.plot(x,y1,'bo-')

                                l3 = plt.plot(x, y3,'r+',label='AGP_iter40', zorder = 11, alpha = 0.6)
                                plt.plot(x,y3,'r+-', zorder = 11)

                                # l1 = plt.plot(x, y1,'bo',label='AGP_S2', zorder = 10, alpha = 0.6)
                                # plt.plot(x,y1,'bo-')

                                # l4 = plt.plot(x, y4,'^', color='lawngreen', label='Discrete_S1', zorder = 10, alpha = 0.6)
                                # plt.plot(x,y4,'^-', color='lawngreen',)

                                # l5 = plt.plot(x, y5,'y^',label='Discrete_S2', zorder = 10)
                                # plt.plot(x,y5,'y^-')

                                # l6 = plt.plot(x, y6,'k^',label='Discrete_S3', zorder = 10)
                                # plt.plot(x,y6,'k^-')

                                # l7 = plt.plot(x, y7,'^', color='tan', label='Discrete_S4', zorder = 10)
                                # plt.plot(x,y7,'^-', color='tan')

                                l2 = plt.plot(x, y2,'g^',label='Discrete_S3', zorder = 10)
                                plt.plot(x,y2,'g^-')

                                plt.scatter(max_indx1+1, y1[max_indx1], 70, marker='x', color = 'black', zorder = 20)
                                plt.annotate(r'Continuous: ['+str(max_indx1)+', '+str("%.4f"%y1[max_indx1])+']',
                                            xy=(max_indx1+1, y1[max_indx1]), xycoords='data',
                                            xytext=(-50, +65), textcoords='offset points', fontsize=9,
                                            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

                                # plt.scatter(max_indx1+1, y1[max_indx1], 70, marker='x', color = 'black', zorder = 20)
                                # plt.annotate(r'AGP_S2: ['+str(max_indx1)+', '+str("%.4f"%y1[max_indx1])+']',
                                #             xy=(max_indx1+1, y1[max_indx1]), xycoords='data',
                                #             xytext=(-200, +0), textcoords='offset points', fontsize=9,
                                #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

                                plt.scatter(max_indx2+1, y2[max_indx2], 70, marker='x', color = 'black', zorder = 20)
                                plt.annotate(r'Discrete_S3: ['+str(max_indx2)+', '+str("%.4f"%y2[max_indx2])+']',
                                            xy=(max_indx2+1, y2[max_indx2]), xycoords='data',
                                            xytext=(-40, +60), textcoords='offset points', fontsize=9,
                                            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

                                plt.scatter(max_indx3+1, y3[max_indx3], 70, marker='x', color = 'black', zorder = 20)
                                plt.annotate(r'AGP_iter40: ['+str(max_indx3)+', '+str("%.4f"%y3[max_indx3])+']',
                                            xy=(max_indx3+1, y3[max_indx3]), xycoords='data',
                                            xytext=(-40,40), textcoords='offset points', fontsize=9,
                                            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
                                
                                # plt.scatter(max_indx4+1, y4[max_indx4], 70, marker='x', color = 'black', zorder = 20)
                                # plt.annotate(r'Discrete_S1: ['+str(max_indx4)+', '+str("%.4f"%y4[max_indx4])+']',
                                #             xy=(max_indx4+1, y4[max_indx4]), xycoords='data',
                                #             xytext=(-160, -10), textcoords='offset points', fontsize=9,
                                #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
                                
                                # plt.scatter(max_indx5+1, y5[max_indx5], 70, marker='x', color = 'black', zorder = 20)
                                # plt.annotate(r'Discrete_S2: ['+str(max_indx5)+', '+str("%.4f"%y5[max_indx5])+']',
                                #             xy=(max_indx5+1, y5[max_indx5]), xycoords='data',
                                #             xytext=(+20, +70), textcoords='offset points', fontsize=9,
                                #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
                                
                                # plt.scatter(max_indx6+1, y6[max_indx6], 70, marker='x', color = 'black', zorder = 20)
                                # plt.annotate(r'Discrete_S3: ['+str(max_indx6)+', '+str("%.4f"%y6[max_indx6])+']',
                                #             xy=(max_indx6+1, y6[max_indx6]), xycoords='data',
                                #             xytext=(-50, +70), textcoords='offset points', fontsize=9,
                                #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

                                # plt.scatter(max_indx7+1, y7[max_indx7], 70, marker='x', color = 'black', zorder = 20)
                                # plt.annotate(r'Discrete_S4: ['+str(max_indx7)+', '+str("%.4f"%y7[max_indx7])+']',
                                #             xy=(max_indx7+1, y7[max_indx7]), xycoords='data',
                                #             xytext=(-20, +50), textcoords='offset points', fontsize=9,
                                #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


                                # plt.title('Fitness of Experiment1 (Continuous)')
                                # plt.title('Fitness of Experiment1 (Discrete)')
                                # plt.title('Fitness of Experiment1 (AGP_S1/AGP_S2)')
                                plt.title('Fitness of Experiment12 (Continuous/Discrete_3/AGP_iter40)')
                                # plt.title('Fitness of Experiment9 (Continuous/Discrete_All/AGP_S1)')



                                plt.xlabel('Number of iterations')
                                plt.ylabel('Fitness')
                                plt.legend()
                                plt.show()


if __name__ == "__main__":
    main()