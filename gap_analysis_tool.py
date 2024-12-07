import pandas as pd

# 점검표 데이터 로드
def load_checklist(file_path):
    """
    Load the checklist data from an Excel file.
    """
    return pd.read_excel(file_path)

# GAP 분석 수행
def perform_gap_analysis(checklist):
    """
    Perform GAP analysis by comparing current status with requirements.
    """
    checklist['Gap'] = checklist['Requirement'] - checklist['Current Status']
    checklist['Compliance'] = checklist['Gap'].apply(lambda x: 'Compliant' if x == 0 else 'Non-Compliant')
    return checklist

# 결과 저장
def save_results_to_excel(dataframe, output_path):
    """
    Save the GAP analysis results to an Excel file.
    """
    dataframe.to_excel(output_path, index=False)
    print(f"Results saved to {output_path}")

# 실행
if __name__ == "__main__":
    # 파일 경로
    input_file = "input_files/checklist_input.xlsx"  # 입력 파일
    output_file = "output_files/gap_analysis_results.xlsx"  # 결과 파일
    
    # 점검표 로드
    checklist_df = load_checklist(input_file)
    
    # GAP 분석
    results_df = perform_gap_analysis(checklist_df)
    
    # 결과 저장
    save_results_to_excel(results_df, output_file)
