# quality-digital-twin
・大学のネットワークに入って、実行してください。
 ※大学のサーバーの中にある、DBを使用しているため

・データベース変更点
 supportテーブルのsontributionでfloat[0,1]ではなく、integer[0,3]としてます

・実行方法
app.pyを実行してください。
➀プロジェクト名＆カテゴリを入力
➁現在のスプリント(`current state`)を1以上に変更することにより、各メニュー（Create Category以外）のボタンを押すことが可能
※Create Categoryはプロジェクト名などを入力しなくても押すことが可能

・各ボタン
Sprint Planning: 品質状態モデルの編集/表示
Dashboard: ダッシュボートの表示（現在、スプリントの達成度のみ表示可能）
QDT-DB: 指定したプロジェクトの情報表示（nodeなどのデータ）
Create Category: QC-DB.db（各重要度のデータベース）を作成



