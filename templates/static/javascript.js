function divide() {
            var txt;
            txt = document.getElementById('preparo').value;
            var text = txt.split(".");
            var str = text.join('.</br>');
            document.write(str);
        }
