<template>
    <div id="start">
        <div id="iconsinicio">
            
        </div>
        <div id="textinicio">
            <h1>FÁBIO CARVALHO</h1>
            <h2>PORTIFÓLIO</h2>
        </div>
        <div id="fotoperfil">
            <img id="imgperfil" src="../assets/img/fabio-perfil.png" alt="perfil">
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>



    #start {
        font-size: 62.5%;
        display: grid;
        grid-auto-columns: 40% 60%;
        grid-template-rows: 20vh 80vh;
        grid-template-areas: 
        "iconsinicio iconsinicio"
        "textinicio fotoperfil"
        ;

        background-image: url('../assets/img/capa.png');
        background-repeat: space;
        height: 100vh;
        width: 100%;
    }

    h1, h2 {
        color: white;
    }

    

    #iconsinicio {
        grid-area: iconsinicio;
    }

    #textinicio {
        grid-area: textinicio;

    }
    
    #fotoperfil {
        grid-area: fotoperfil;

    }


    #imgperfil {
        height: 80vh;
        width: 80vw;
        max-width: 600px;

        
        
    }
</style>