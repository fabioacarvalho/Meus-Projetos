<template>
    <div class="general container-fluid">
        <div class="header" >
            <a target="_blank" href="https://github.com/fabioacarvalho">
                <img class="img-fluid" id="linkgituhub" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" data-canonical-src="https://img.shields.io/badge/github-%23100000.svg?&amp;style=for-the-badge&amp;logo=github&amp;logoColor=white&amp;link=mailto:https://github.com/fabioacarvalho">
            </a>             
            <a target="_blank" href="mailto:fabio22191@gmail.com">
                <img class="img-fluid" id="linkgmail" src="https://www.vectorlogo.zone/logos/gmail/gmail-tile.svg" data-canonical-src="https://img.shields.io/badge/gmail-D14836?&amp;style=for-the-badge&amp;logo=gmail&amp;logoColor=white&amp;link=mailto:fabio22191@gmail.com">
            </a>             
            <a target="_blank" href="https://www.linkedin.com/in/fabio-carvalho-881026142/" rel="nofollow">
                <img class="img-fluid" id="linklinkedin" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-tile.svg" data-canonical-src="https://img.shields.io/badge/linkedin-%230077B5.svg?&amp;style=for-the-badge&amp;logo=linkedin&amp;logoColor=white&amp;link=mailto:https://www.linkedin.com/in/fabio-carvalho-881026142/">
            </a>

        </div>
        <div class="container-fluid">
            <img id="fotofabio" class="img-fluid" src="../assets/imagens/fabio-perfil.png" alt="Perfil">
            <h1 id="nome">FÁBIO</h1>
            <h1 id="sobrenome">CARVALHO</h1>
            <h2 id="portifolio">PORTIFÓLIO</h2>
        </div>
        
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
               
    }

    div, .general {
        background-image: url("../assets/imagens/capa.png");
        background-repeat: no-repeat;
    }
    

    #fotofabio {
        display: flex;
        float: right;
        position: relative;
        background: transparent;
        /* height: 700px;*/
        width: 800px; 
        padding-top: 68px;
        z-index: 9000;

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
        /* height: 50px; */
        width: 50px;
        background: transparent;
        float: right;
        margin: 0px 180px -50px 0px;
        z-index: 10000;
    }

    #linkgmail {
        /* height: 50px; */
        width: 50px;
        background: transparent;
        float: right;
        margin: 0px 110px -50px 0px;
        z-index: 10000;
    }

    #linkgituhub {
        /* height: 50px; */
        width: 50px;
        background: transparent;
        float: right;
        margin: 0px 250px -50px 0px;
        z-index: 10000;
    }

    

</style>