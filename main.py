def Pivot_Point(H, L, C):
    
        import pandas as pd
 
####### this is the Standard formula ########
        PP = (H+L+C)/3
        R1 = (2*PP)-L
        S1 = (2*PP)-H
        R2 = (PP-S1)+R1
        S2 = PP - (R1-S1)
        R3 = R2 + (H-L)
        S3 = S2 -(H-L)
###### this is the formula of Fibonacci ########
        PP_1 = (H + L + C) / 3
        R1_1 = PP_1 + 0.382 * (H - L)
        S1_1 = PP_1 - 0.382 * (H - L)
        R2_1 = PP_1 + 0.618 * (H - L)
        S2_1 = PP_1 - 0.618 * (H - L)
        R3_1 = PP_1 + (H - L)
        S3_1 = PP_1 - (H - L)
##### this is the formula of  Camarilla #######
        PP_2 = (H + L + C) / 3
        R1_2 = C + (0.0916 * (H - L))
        S1_2 = C - (0.0916 * (H - L))
        R2_2 = C + (0.183 * (H - L))
        S2_2 = C - (0.183 * (H - L))
        R3_2 = C + (0.275 * (H - L))
        S3_2 = C - (0.275 * (H - L))
        R4_2 = C + (0.55 * (H - L))
        S4_2 = C - (0.55 * (H - L))
###### this is the formula of Woodies #######
        PP_3 = (H + L + (2 * C)) / 4
        R1_3 = (2 * PP_3) - L
        S1_3 = (2 * PP_3) - H
        R2_3 = PP_3 + (H - L)
        S2_3 = PP_3 - (H - L)
        R3_3 = H + 2 * (PP_3 - L)
        S3_3 = L - 2 * (H - PP_3)

####### list of the name of the formual ##########
        formula = ["Standard","Fibonacci", "Camarilla", "Woodies"]
###### dictionary of the indicator ###########
        indicator =  {"Pivot"  :  [round(PP,2), round(PP_1,2), round(PP_2,2),round(PP_3,2)],
                    "R1" : [round(R1,2),round(R1_1,2),round(R1_2,2),round(R1_3,2)],
                   "S1" : [round(S1,2),round(S1_1,2), round(S1_2,2),round(S1_3,2)],
                    "R2 " : [round(R2,2),round(R2_1,2), round(R2_2,2),round(R2_3,2)],
                    "S2 " : [round(S2,2),round(S2_1,2), round(S2_2,2),round(S2_3,2)],
                    "R3 "  : [round(R3,2),round(R3_1,2),round(R3_2,2),round(R3_3,2)],
                    "S3 "  : [round(S3,2),round(S3_1,2), round(S3_2,2),round(S3_3,2)]} 

        table = pd.DataFrame(indicator, index=formula)
        return table
