var selected="all"


$(document).ready(function(){
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/api/google/", true);
    xmlhttp.send();
    
    var xmlhttp2=new XMLHttpRequest();
    xmlhttp2.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp2.open("GET", "http://127.0.0.1:8000/api/apple/", true);
    xmlhttp2.send();

    var xmlhttp3=new XMLHttpRequest();
    xmlhttp3.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp3.open("GET", "http://127.0.0.1:8000/api/microsoft/", true);
    xmlhttp3.send();

    var xmlhttp4=new XMLHttpRequest();
    xmlhttp4.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp4.open("GET", "http://127.0.0.1:8000/api/meta/", true);
    xmlhttp4.send();
});

function allnews(){
    selected="all"
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            $("#tablebod").html("");
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/api/google/", true);
    xmlhttp.send();
    
    var xmlhttp2=new XMLHttpRequest();
    xmlhttp2.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp2.open("GET", "http://127.0.0.1:8000/api/apple/", true);
    xmlhttp2.send();

    var xmlhttp3=new XMLHttpRequest();
    xmlhttp3.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp3.open("GET", "http://127.0.0.1:8000/api/microsoft/", true);
    xmlhttp3.send();

    var xmlhttp4=new XMLHttpRequest();
    xmlhttp4.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp4.open("GET", "http://127.0.0.1:8000/api/meta/", true);
    xmlhttp4.send();
}


function getnews(comp) {
    selected=comp
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            
            // l=JSON.parse(this.responseText);
            // document.getElementById("tablebod").innerHTML=l
            var json=JSON.parse(this.responseText)
            $("#tablebod").html("<tr>");
            for(var i=0;i<json.length;i++)
            {
                $("#tablebod").append("<tr>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].query);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].title);
                $("#tablebod").append("</td>");
                $("#tablebod").append("<td>");
                $("#tablebod").append(json[i].ago);
                $("#tablebod").append("</td>");
                $("#tablebod").append("</tr>");
            }
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/api/"+comp+"/", true);
    xmlhttp.send();
}

function filter() {
    date1=document.getElementById("from").value;
    date2=document.getElementById("to").value;
    alert(date1);
    alert(date2);
}