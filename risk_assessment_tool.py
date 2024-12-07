import pandas as pd

# 리스크 평가 도구
def load_risk_data(file_path):
    """
    Load risk data (assets, threats, vulnerabilities) from an Excel file.
    """
    return pd.read_excel(file_path)

def calculate_risk_score(data):
    """
    Calculate risk score based on likelihood and impact.
    """
    data['Risk Score'] = data['Likelihood'] * data['Impact']
    return data

def suggest_mitigation(data):
    """
    Suggest mitigation actions based on risk scores.
    """
    data['Mitigation'] = data['Risk Score'].apply(lambda x: 'High Priority Mitigation' if x > 15 else 'Monitor')
    return data

def save_results_to_excel(dataframe, output_path):
    """
    Save the risk assessment results to an Excel file.
    """
    dataframe.to_excel(output_path, index=False)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    # 파일 경로
    input_file = "input_files/risk_data.xlsx"  # 리스크 입력 파일
    output_file = "output_files/risk_analysis_results.xlsx"  # 결과 파일

    # 리스크 데이터 로드
    risk_data_df = load_risk_data(input_file)

    # 리스크 분석
    risk_data_df = calculate_risk_score(risk_data_df)
    risk_data_df = suggest_mitigation(risk_data_df)

    # 결과 저장
    save_results_to_excel(risk_data_df, output_file)
