from spyre import server
import pandas


class VHIApp(server.App):
    title = "VHI App"

    inputs = [{"type": 'dropdown', "label": 'Time row', "value": 'VHI',
               "options": [{"label": "VHI", "value": "VHI"},
                           {"label": "VCI", "value": "VCI"},
                           {"label": "TCI", "value": "TCI"}], "key": 'number'},

              {"type": 'dropdown', "label": 'District', "value": 'Kiev',
               "options": [{"label": "Vinnytsya", "value": "Vinnytsya"},
                           {"label": "Volyn", "value": "Volyn"},
                           {"label": "Dnipropetrovsk", "value": "Dnipropetrovsk"},
                           {"label": "Donetsk", "value": "Donetsk"},
                           {"label": "Zhytomyr", "value": "Zhytomyr"},
                           {"label": "Zacarpathia", "value": "Zacarpathia"},
                           {"label": "Zaporizhzhya", "value": "Zaporizhzhya"},
                           {"label": "Ivano-Frankivsk", "value": "Ivano-Frankivsk"},
                           {"label": "Kiev", "value": "Kiev"},
                           {"label": "Kirovograd", "value": "Kirovograd"},
                           {"label": "Lviv", "value": "Lviv"},
                           {"label": "Mykolayiv", "value": "Mykolayiv"},
                           {"label": "Odessa", "value": "Odessa"},
                           {"label": "Poltava", "value": "Poltava"},
                           {"label": "Rivne", "value": "Rivne"},
                           {"label": "Sumy", "value": "Sumy"},
                           {"label": "Ternopil", "value": "Ternopil"},
                           {"label": "Kharkiv", "value": "Kharkiv"},
                           {"label": "Kherson", "value": "Kherson"},
                           {"label": "Khmel'nyts'kyy", "value": "Khmel'nyts'kyy"},
                           {"label": "Cherkasy", "value": "Cherkasy"},
                           {"label": "Chernivtsi", "value": "Chernivtsi"},
                           {"label": "Chernihiv", "value": "Chernihiv"},
                           {"label": "Crimea", "value": "Crimea"}], "key": 'region'},

              {"type": "slider", "label": 'Width of line', "key": "width", "value": '1',
               "min": 1, "max": 10, "action_id": "width"},
              {"type": "text", "label": 'Year #1', "key": "year1", "value": '2007'},
              {"type": "text", "label": 'Year #2', "key": "year2", "value": '2008'},
              {"type": "text", "label": 'Interval of weeks from', "key": "w1", "value": '1'},
              {"type": "text", "label": 'to', "key": "w2", "value": '52'}]

    controls = [{"type": "button", "label": "Create a graph", "id": "submit_plot"}]
    tabs = ["Graph1", "Graph2", "Table1", "Table2"]
    outputs = [{"type": "plot", "id": "plot", "control_id": "submit_plot", "tab": "Graph1"},
               {"type": "plot", "id": "plot1", "control_id": "submit_plot", "tab": "Graph2"},
               {"type": "table", "id": "table", "control_id": "submit_plot", "tab": "Table1", "on_page_load": True},
               {"type": "table", "id": "table1", "control_id": "submit_plot", "tab": "Table2", "on_page_load": True}]

    def table(self, params):
        check_params(params)
        df = pandas.read_csv("/home/KPI2course/SRP/Lab2/data.csv", encoding='utf-8')
        df = df.drop('Unnamed: 0', 1)
        df = df[(df['region'] == params['region']) & (df['year'] == int(params['year1'])) &
                (df['week'] >= int(params['w1'])) & (df['week'] <= int(params['w2']))]
        return df

    def table1(self, params):
        check_params(params)
        df = pandas.read_csv("/home/KPI2course/SRP/Lab2/data.csv", encoding='utf-8')
        df = df.drop('Unnamed: 0', 1)
        df = df[(df['region'] == params['region']) & (df['year'] == int(params['year2'])) &
                (df['week'] >= int(params['w1'])) & (df['week'] <= int(params['w2']))]
        return df

    def plot(self, params):
        df = self.table(params)
        plt = df.plot(x='week', y=params['number'], linewidth=params['width'])
        plt.set_title(params['year1'])
        return plt.get_figure()

    def plot1(self, params):
        df = self.table1(params)
        plt = df.plot(x='week', y=params['number'], linewidth=params['width'])
        plt.set_title(params['year2'])
        return plt.get_figure()


def check_params(params):
    if int(params['year1']) < 1981: params['year1'] = 1981
    if int(params['year1']) > 2016: params['year1'] = 2016
    if int(params['year2']) < 1981: params['year2'] = 1981
    if int(params['year2']) > 2016: params['year2'] = 2016

    if int(params['w1']) < 1: params['w1'] = 1
    if int(params['w2']) > 52: params['w2'] = 52
    if int(params['w1']) > int(params['w2']):
        params['w1'] = 1
        params['w2'] = 52

app = VHIApp()
app.launch()
                          

    
       

   
