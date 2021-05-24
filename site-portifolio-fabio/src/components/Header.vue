<template>
    <div >
        <div class="header">
            <a href="#"><img id="linkgituhub" src="../assets/icons/github-tile.svg" alt="Github"></a>
            <a href="#"><img id="linklinkedin" src="../assets/icons/linkedin-tile.svg" alt="Github"></a>
            <a href="#"><img id="linkgmail" src="../assets/icons/gmail-icon.svg" alt="Github"></a>
        </div>
        <img id="fotofabio" src="../assets/imagens/fabio-perfil.png" alt="Perfil">
        <h1 id="nome">FÁBIO</h1>
        <h1 id="sobrenome">CARVALHO</h1>
        <h2 id="portifolio">PORTIFÓLIO</h2>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>

    * {
        padding: 0px;
        margin: 0px;
        background-image: url("../assets/imagens/capa.png");
        background-repeat: no-repeat;
        
    }
    

    #fotofabio {
        display: flex;
        float: right;
        position: relative;
        background: transparent;
        height: 700px;
        width: 800px;
        padding-top: 10px;

    }

    #nome {
        padding-top: 150px;
    }

    #portifolio {
        display: flex;
        color: white;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        float: left;
        background: transparent;
        font-size: 40px;
        flex-wrap: wrap;
        padding-left: 50px;
    }

    #nome, #sobrenome {
        display: flex;
        color: white;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        float: left;
        background: transparent;
        font-size: 90px;
        flex-wrap: wrap;
        padding-left: 50px;
        
    }

    #linklinkedin {
        height: 50px;
        width: 50px;
        background: transparent;
        float: right;
        margin: -50px 180px -50px 0px;
        z-index: 10000;
    }

    #linkgmail {
        height: 50px;
        width: 50px;
        background: transparent;
        float: right;
        margin: -50px 110px -50px 0px;
        z-index: 10000;
    }

    #linkgituhub {
        height: 50px;
        width: 50px;
        background: transparent;
        float: right;
        margin: -50px 250px -50px 0px;
        z-index: 10000;
    }

</style>