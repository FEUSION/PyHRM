########################################################################################################################
##Importing Libraries
import sys
import PIL
import subprocess
import warnings
warnings.filterwarnings('ignore')
try:
    import pandas as pd
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pandas'])
    import pandas as pd
try:
    import numpy as np
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','numpy'])
    import numpy as np
try:
    import xlrd
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xlrd'])
    import xlrd
try:
    import plotly
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'plotly'])
try:
    import openpyxl
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])
try:
    import scipy
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scipy'])
import plotly.graph_objects as go
import plotly.express as px

########################################################################################################################


class MeltcurveInterpreter:

    def __init__(self):
        # lables
        self.labels = []
        # Data Frame after processed
        self.transformed_data = pd.DataFrame()
        self.processed_data = pd.DataFrame()

    def data_read(self, path, labels=False, index = False):
        try:
            try:
                return_data = pd.read_excel(path, engine='xlrd')
            except:
                return_data = pd.read_excel(path)
        except:
            raise ValueError("Unsupported Format!")

        if index:
            return_data.drop(return_data.columns[0], axis =1, inplace= True)

        if not all([return_data.columns[0] == 'Text', return_data.columns[1] == 'X', return_data.columns[2] == 'Y',
                    return_data.columns[3] == 'Text.1']):
            raise ValueError("""Could not Load:
                                1. Please check your input spreadsheet format. 
                                    If your input file has index, please assign "index=True".
                                2.Or Invalid File""")

        for cols in return_data.iloc[:, 0::3].columns:
            self.labels.append(return_data[cols].unique()[0])
        dummy_data = pd.concat([return_data.iloc[:, 1], return_data.iloc[:, 2::3]], axis=1)
        del return_data
        return_data = dummy_data
        self.transformed_data = return_data

        if labels:
            return [self.transformed_data, np.array(self.labels).reshape(-1)]
        else:
            return self.transformed_data

    def plot(self):

        from PIL import Image
        import requests
        from io import BytesIO
        response = requests.get("https://microlabindia.com/wp-content/uploads/2022/06/MBL-Logo.png")
        img = Image.open(BytesIO(response.content))

        fig = go.Figure()
        for X in range(1, len(self.transformed_data.columns)):
            fig.add_trace(go.Scatter(x=self.transformed_data.iloc[:, 0],
                                     y=self.transformed_data.iloc[:, X],
                                     name=self.labels[X-1]))
            if self.transformed_data.iloc[1,1]>20.0:
                title = "<i><b>Raw Fluorescence Curve</b></i>"
                ytitle = "Fluorescence"
                xtitle = 'Temperature in Celsius'
            elif self.transformed_data.iloc[0,0]==1:
                title = "<i><b>Amplification Curve</b></i>"
                ytitle = "Normalized Fluorescence"
                xtitle = 'Cycle Time'
            else:
                title = "<i><b>Melt Curve</b></i>"
                ytitle = 'dF/dT'
                xtitle = 'Temperature in Celsius'
            fig.update_layout(title_text=(title),
                              title_x = 0.22,
                              title_font_size=30,
                              title_font_family='Arial',
                              legend_itemclick="toggleothers",
                              legend_itemdoubleclick="toggleothers",
                              legend_groupclick="togglegroup",
                              legend_title_text='<b>Targets<b>',
                              legend_font_size=12,
                              legend_title_font_family='Arial',
                              legend_title_font_size=18,
                              legend_bgcolor="#f1f1f1",
                              legend_borderwidth=1,
                              plot_bgcolor='#000000',
                              title_font_color="#417a41",
                              )
            fig.update_xaxes(title_text =xtitle,
                             showgrid = False)
            fig.update_yaxes(title_text =ytitle,
                             showgrid= False)
            fig.layout.images = [dict(source=img,
                                      xref="paper",
                                      yref="paper",
                                      x=0.1,
                                      y=1.05,
                                      sizex=0.20,
                                      sizey=0.20,
                                      xanchor="center",
                                      yanchor="bottom")]
        fig.show()


    def melt_convertion(self):
        data_copy = self.transformed_data.copy()
        # for columns in data_copy.columns[1:]:
        #     data_copy[columns] = ((data_copy[columns] - data_copy[columns].min())/(data_copy[columns].max() - data_copy[columns].min()))*10
        #     #data_copy[columns] = data_copy[columns]/data_copy[columns].max()
        # print(data_copy)

        for columns in data_copy.columns[1:]:
            # for i in range(0, len(data_copy[columns])):
                # if i != len(data_copy[columns])-1:
                #     difference = (data_copy[columns][i] - data_copy[columns][i+1])/(data_copy.iloc[i,0] - data_copy.iloc[i+1,0])
                #     diff_list.append(-difference)
                # else:
                #     difference = data_copy[columns][i]/data_copy.iloc[i,0]
                #     diff_list.append(-difference)
            diff = np.gradient(data_copy[columns], data_copy.iloc[:,0])
            data_copy[columns] = -diff
        new_df = pd.DataFrame(columns = data_copy.columns)
        xnew = np.linspace(70.00, 95.00, 748)
        new_df['X'] = xnew
        for cols in data_copy[1:]:
            splrep = scipy.interpolate.splrep(data_copy.iloc[:,0], data_copy[cols], s = 0.031)
            new_df[cols] = scipy.interpolate.splev(xnew,splrep)
        self.processed_data = new_df

    def plot_after(self):

        import PIL
        from PIL import Image
        import requests
        from io import BytesIO
        response = requests.get("https://microlabindia.com/wp-content/uploads/2022/06/MBL-Logo.png")
        img = Image.open(BytesIO(response.content))

        fig2 = go.Figure()
        for X in range(1, len(self.processed_data.columns)):
            fig2.add_trace(go.Scatter(x=self.processed_data.iloc[:, 0],
                                     y=self.processed_data.iloc[:, X],
                                     name=self.labels[X-1]))
            if self.processed_data.iloc[1,1]>20.0:
                title = "<i><b>Raw Fluorescence Curve</b></i>"
                ytitle = "Fluorescence"
                xtitle = 'Temperature in Celsius'
            elif self.processed_data.iloc[0,0]==1:
                title = "<i><b>Amplification Curve</b></i>"
                ytitle = "Normalized Fluorescence"
                xtitle = 'Cycle Time'
            else:
                title = "<i><b>Melt Curve</b></i>"
                ytitle = 'dF/dT'
                xtitle = 'Temperature in Celsius'
            fig2.update_layout(title_text=(title),
                              title_x = 0.22,
                              title_font_size=30,
                              title_font_family='Arial',
                              legend_itemclick="toggleothers",
                              legend_itemdoubleclick="toggleothers",
                              legend_groupclick="togglegroup",
                              legend_title_text='<b>Targets<b>',
                              legend_font_size=12,
                              legend_title_font_family='Arial',
                              legend_title_font_size=18,
                              legend_bgcolor="#f1f1f1",
                              legend_borderwidth=1,
                              plot_bgcolor='#000000',
                              title_font_color="#417a41",
                              )
            fig2.update_xaxes(title_text =xtitle,
                             showgrid = False)
            fig2.update_yaxes(title_text =ytitle,
                             showgrid= False)
            fig2.layout.images = [dict(source=img,
                                      xref="paper",
                                      yref="paper",
                                      x=0.1,
                                      y=1.05,
                                      sizex=0.20,
                                      sizey=0.20,
                                      xanchor="center",
                                      yanchor="bottom")]
        fig2.show()










