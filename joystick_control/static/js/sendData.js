var oldX=0
var oldY=0

function sendDataToServer() {
    const joy1X = document.getElementById('joy1X');
    const joy1Y = document.getElementById('joy1Y');
    const x_axis = joy1X.value;
    const y_axis = joy1Y.value;
    
    // if(x_axis!=oldX || y_axis!=oldY){
    
    //     oldX=x_axis;
    //     oldY=y_axis;
    // 送信するデータ
    const data = {
        x_axis: x_axis,
        y_axis: y_axis,    
    
    };
    //urlから送信先のIPアドレスを取得
    post_ip = location.href;
    console.log(post_ip+"")
    // サーバへのPOSTリクエストを送信
    fetch(post_ip+"/receiveData", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

// 毎秒データを送信する
setInterval(sendDataToServer, 300);