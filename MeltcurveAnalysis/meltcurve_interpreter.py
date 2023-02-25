########################################################################################################################
##Importing Libraries
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')
subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
try:
    import packaging
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'packaging'])
try:
    import pandas as pd
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pandas'])
    import pandas as pd
try:
    import PIL
    import requests
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pillow'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    import PIL
    import requests
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
    from scipy.signal import find_peaks, peak_widths
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scipy'])
    import scipy
    from scipy.signal import find_peaks, peak_widths
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
########################################################################################################################


class MeltcurveInterpreter:

    def __init__(self):
        # lables
        self.labels = []
        # Data Frame after processed
        self.transformed_data = pd.DataFrame()
        self.processed_data = pd.DataFrame()

    def plot(self, data):

        from PIL import Image
        import requests
        from io import BytesIO
        response = requests.get("https://microlabindia.com/wp-content/uploads/2022/06/MBL-Logo.png")
        img = Image.open(BytesIO(response.content))

        fig = go.Figure()
        for X in range(1, len(data.columns)):
            fig.add_trace(go.Scatter(x=data.iloc[:, 0],
                                     y=data.iloc[:, X],
                                     name=self.labels[X-1]))
            if data.iloc[1,1]>20.0:
                title = "<i><b>Raw Fluorescence Curve</b></i>"
                ytitle = "Fluorescence"
                xtitle = 'Temperature in Celsius'
            elif data.iloc[0,0]==1:
                title = "<i><b>Amplification Curve</b></i>"
                ytitle = "Normalized Fluorescence"
                xtitle = 'Cycle Time'
            else:
                title = "<i><b>Melt Curve</b></i>"
                ytitle = 'dF/dT'
                xtitle = 'Temperature in Celsius'
            fig.update_layout(title_text=(title),
                              title_x = 0.5,
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

    def data_read(self, path, labels=False, index=False, figure=False):
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

        if figure:
            self.plot(data=self.transformed_data)

        if labels:
            return [self.transformed_data, np.array(self.labels).reshape(-1)]
        else:
            return self.transformed_data

    def melt_convertion(self, figure = False, return_value = False):
        data_copy = self.transformed_data.copy()

        for columns in data_copy.columns[1:]:
            diff = np.gradient(data_copy[columns], data_copy.iloc[:,0])
            data_copy[columns] = -diff/10
        new_df = pd.DataFrame(columns = data_copy.columns)
        xnew = np.linspace(data_copy.iloc[0,0], data_copy.iloc[-1,0], int(len(data_copy.iloc[:,0])*2.945))
        new_df['X'] = xnew
        for cols in data_copy[1:]:
            splrep = scipy.interpolate.splrep(data_copy.iloc[:,0], data_copy[cols], s = 0.031)
            new_df[cols] = scipy.interpolate.splev(xnew,splrep)
        self.processed_data = new_df

        if figure:
            self.plot(data = self.processed_data)

        if return_value:
            return self.processed_data


    # def feature_detection(self):
    #     n = 2
    #     #  plt.figure(figsize=(50, 150))
    #     for k in range(1, len(data.columns)):
    #         ## find peaks
    #         peaks = find_peaks(data.iloc[:, k], 2)
    #
    #         sorted_heights = np.sort(list(peaks[1].values())[0])[::-1]
    #         sorted_x = [float(data.iloc[:, 0][data.iloc[:, k] == o]) for o in sorted_heights]
    #         final_peaks = [data.iloc[:, 0][data.iloc[:, 0] == t].index[0] for t in sorted_x][:n]
    #         sorted_heights = sorted_heights[:n]
    #         sorted_x = sorted_x[:n]
    #         ## peak width
    #
    #         res = peak_widths(data.iloc[:, k], final_peaks, rel_height=0.75)
    #         plt.subplot(18, 3, k)
    #         plt.plot(data.iloc[:, 0], data.iloc[:, k])
    #         plt.scatter(sorted_x, sorted_heights, color='red')
    #         start_indices = [data.iloc[round(ele), 0] for ele in res[2]]
    #         end_indices = [data.iloc[round(ele), 0] for ele in res[3]]
    #
    #         # plotting start end points
    #
    #         for ele3, ele4 in zip(start_indices, res[1]):
    #             plt.scatter(ele3, ele4, color='green')
    #         for ele3, ele4 in zip(end_indices, res[1]):
    #             plt.scatter(ele3, ele4, color='orange')
    #
    #         final_res = (res[1], start_indices, end_indices)
    #         for ele1, ele2 in zip(sorted_x, sorted_heights):
    #             plt.vlines(x=ele1, ymin=0, ymax=ele2, linestyles='dashed')
    #         plt.hlines(*final_res, color='blue')
    #         plt.legend(['Derivative Plot', f'Peak: {sorted_x}', f'Start: {start_indices}', f'End: {end_indices}',
    #                     f'Height: {sorted_heights}'])
    #         # print(f'Peak (Tm) : {sorted_x}')
    #         # eplt.savefig('17 CODING K.PNEUMOAND A.BAUMANII RUN FILE 05022023 (67 RXNS) Melt.png')




