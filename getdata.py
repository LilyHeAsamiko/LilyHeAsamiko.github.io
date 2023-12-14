import tushare as ts

def get_data(code):
    dict_return = {} # �����Ҫ������
    data = ts.get_hist_data(code) # ͨ����Ʊ�����ȡ��Ʊ���������
    data_30 = data[:30].iloc[::-1] # ��������������������
    data_30['rise'] = data_30['price_change'] > 0 # ��
    data_30['fall'] = data_30['price_change'] < 0 # ��
    close = data_30['close'] #���30�������յ����̼�
    close_index = list(close.index) # ���̼�x������
    close_value = close.values.tolist() # ���̼�y������
    df_diff = data_30[['rise','fall']].sum() # ͳ�ƽ�30�����յ��ǵ�����
    df_diff_index = list(df_diff.index) # ������תΪ�б��ʽ
    df_diff_value = df_diff.values.tolist() # ������תΪ�б��ʽ
    dict_return['diff'] = [{"name":item[0],"value":item[1]} for item in list(zip(df_diff_index,df_diff_value))] # �����������ɱ�ͼ��Ҫ�����ݸ�ʽ
    price_change = data_30['price_change'].values.tolist() # ͳ�ƽ�30�����յļ۸�仯
    volume = data_30['volume'].values.tolist() # ͳ�ƽ�30�����յĳɽ���
    # ����Ϊ������õ����ݼ����ֵ�
    dict_return['close_index'] = close_index 
    dict_return['close_value'] = close_value
    dict_return['price_change'] = price_change
    dict_return['volume'] = volume
    dict_return['df_diff_index'] = df_diff_index
    return dict_return
