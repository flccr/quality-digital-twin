def make_options_from_catalog(node_subchar, node_data):
    print(f'node_data : {node_data.id} ')
    options = []
    results = catalog_db.get_catalog_by_subchar(node_subchar)
    print(f'result : {results}')
    options = [{'label': row[0], 'value': row[0], 'extra_data': row[1]} for row in results]
    print("取得したオプション:", options)  

    keywords = extract_keywords(node_data.id)
    print("抽出されたキーワード:", keywords)  

    related_options = []
    # 各オプションに対して関連スコアを計算
    for option in options:
        score = sum(1 for keyword in keywords if keyword in option['extra_data'])  # 一致したキーワードの数をカウント
        if score > 0:  # 一致があれば関連オプションに追加
            related_options.append((score, option))  # スコアとオプションをタプルで追加
            print(f"オプション '{option['label']}' のスコア:", score) 

    # スコアに基づいて関連オプションをソート（スコアの高い順）
    related_options.sort(reverse=True, key=lambda x: x[0])
    print("スコア順にソート後のオプション:", related_options)  

    new_options = []

    # 一番高いスコアを持つものを取得
    if related_options:
        highest_score = related_options[0][0]
        highest_score_options = [opt for score, opt in related_options if score == highest_score]
        
        print("一番高いスコア:", highest_score)  
        print("一番高いスコアの選択肢:", highest_score_options) 

        # new_options.append({'label': '関連性の高い非機能テスト', 'value': '', 'disabled': True, 'style': {'border': '2px solid #ccc', 'padding': '5px'}})
        new_options.append({
                  'label': html.Div('特に関連性の高いテスト', style={'border': '2px solid #228B22', 'padding': '5px', 'margin': '5px 0', 'color':'#000000', 'font-weight': 'bold'}),
                  'value': 0,
                  'disabled': True
              })
        new_options.extend(highest_score_options)
    
        # 次に高いスコアのものを取得（存在する場合のみ）
        next_highest_options = [opt for score, opt in related_options if score < highest_score]
        print("next_highest_options:", next_highest_options)  
        if next_highest_options:
            next_highest_scores = [score for score, opt in related_options if score < highest_score]
            next_highest_score = next_highest_scores[0] if next_highest_scores else None  # 二番目に高いスコアを取得

            print("二番目に高いスコア:", next_highest_score)  
            print("二番目に高いスコアの選択肢:", next_highest_options)  

            if next_highest_score is not None:
                # new_options.append({'label': '関連のありそうな非機能テスト', 'value': '', 'disabled': True, 'style': {'border': '2px solid #ccc', 'padding': '5px'}})
                new_options.append({
                  'label': html.Div('関連性がありそうなテスト', style={'border': '2px solid #FFA500', 'padding': '5px', 'margin': '5px 0', 'color': '#333333'}),
                  'value': 0,
                  'disabled': True
              })
                new_options.extend(next_highest_options)

    # 重複を防ぐためのセットを使用
    seen = set()
    unique_options = []
    for option in new_options:
        option_tuple = (option['label'], option['value'])
        if option_tuple not in seen:
            seen.add(option_tuple)
            unique_options.append(option)

    return unique_options