import sys
import subprocess
try:
    import pandas as pd
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pandas'])
    import pandas as pd
try:
    import xlrd
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xlrd'])
    import xlrd

try:
    import plotly
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'plotly'])

import plotly.graph_objects as go
import plotly.express as px


class MeltcurveInterpreter:

    def __init__(self):
        # lables
        self.labels = []
        self.transformed_data = pd.DataFrame()
        self.maximum_temperatures = []
    # function to read data in excel/csv format

    def data_read(self, path, labels=False):
        try:
            return_data = pd.read_excel(path, engine='xlrd')
        except:
            return_data = pd.read_csv(path)
        for cols in return_data.iloc[:,0::3].columns:
            self.labels.append(return_data[cols].unique()[0])

        # dropping unwanted columns
        dummy_data = pd.concat([return_data.iloc[:,1], return_data.iloc[:, 2::3]], axis = 1)
        del return_data
        return_data = dummy_data
        self.transformed_data = return_data
        if labels:
            return [self.transformed_data, self.labels]
        else:
            return self.transformed_data

    def plot(self):
        fig = go.Figure()
        for X in range(1, len(self.transformed_data.columns)):
            fig.add_trace(go.Scatter(x=self.transformed_data.iloc[:, 0], y=self.transformed_data.iloc[:, X], name=self.labels[X-1]))
            fig.update_layout(title_text = 'Melt Curve', title_font_size=25)
            fig.update_xaxes(title_text = 'Temperature in Celsius')
            fig.update_yaxes(title_text = 'dF/dT')
        return fig

    def peak(self, plot = False):
        for X in range(1, len(self.transformed_data.columns)):
            self.maximum_temperatures.append(
                float(self.transformed_data[self.transformed_data.iloc[:,X] == self.transformed_data.iloc[:,X].max()].iloc[:,0])
            )
        if plot:
            fig1 = px.line(x = self.labels, y = self.maximum_temperatures)
            fig1.update_layout(title_text = 'Peaks', title_font_size =25)
            fig1.update_xaxes(title_text = 'Experiments')
            fig1.update_yaxes(title_text = 'Temperature in Celsius')
            return fig1
        else:
            return self.maximum_temperatures

    def deviations(self):
        result = []
        columns = [column for column in self.transformed_data.iloc[:,1:].columns]

        def deviation_finder(column):

            roc = []
            for i in range(len(self.transformed_data)):
                if i == 0:
                    rate_of_change = 0
                else:
                    rate_of_change = int(self.transformed_data[column][i]/0.05)
                roc.append({i : rate_of_change})

            flat = []
            for ele in roc:
                flat+= ele.values()
            flat_df = pd.DataFrame(flat)
            values_count = flat_df.value_counts()
            keys = list(values_count.to_dict().keys())
            keys = [x[0] for x in keys]
            values = list(values_count.to_dict().values())

            start_end = []
            for a,b in zip(keys, values):
                if 2 < b <= 8:
                    start_end.append({a:b})

            def min_max_finder(start_point):
                Keys = []
                Values = []
                for ele in start_end:




                    Keys.append(list(ele.keys())[0])
                    Values.append(list(ele.values())[0])
                Keys.sort()
                end = Keys[0]
                for element in start_end:
                    if end in element.keys():
                        end_point = element
                        start_end.remove(element)
                        break
                ep = end_point

                del Keys
                del Values

                Keys = []
                Values = []
                for ele1 in start_end:
                    Keys.append(list(ele1.keys())[0])
                    Values.append(list(ele1.values())[0])
                Values.sort(reverse = True)

                start = Values[0]
                for ele2 in start_end:
                    if start in ele2.values():
                        start_point = ele2
                        start_end.remove(ele2)
                sp = start_point

                return [sp,ep]

            start_end_final = min_max_finder(start_end)
            if list(start_end_final[0].keys())[0] > list(start_end_final[1].keys())[0]:
                start_temp = self.transformed_data['X'].iloc[flat.index(list(start_end_final[0].keys())[0])]
            else:
                start_temp = self.transformed_data['X'].iloc[flat.index(list(start_end_final[1].keys())[0])]

            if list(start_end_final[0].keys())[0] < list(start_end_final[1].keys())[0]:
                end_temp = self.transformed_data['X'].iloc[flat.index(list(start_end_final[0].keys())[0])]
            else:
                end_temp = self.transformed_data['X'].iloc[flat.index(list(start_end_final[1].keys())[0])]

            return [start_temp, end_temp]

        for features in columns:
            temp_res = deviation_finder(features)
            result.append(temp_res)
        #
        # if plot:
        #     fig2 = go.Figure()
        #     for X in range(1, len(self.transformed_data.columns)):
        #         fig2.add_trace(go.Scatter(x=self.labels[X - 1], y=self.transformed_data.iloc[:, X],
        #                                  name=self.labels[X - 1]))
        #         fig2.update_layout(title_text='Melt Curve', title_font_size=25)
        #         fig2.update_xaxes(title_text='Temperature in Celsius')
        #         fig2.update_yaxes(title_text='dF/dT')
        #     return fig
        return result