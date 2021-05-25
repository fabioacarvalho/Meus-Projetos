<template>
    <div>
        <h1>Abstract</h1>
        <div id="sobre">
            <section id="skills">
                <div class="quadroum quadro">
                    <img class="firstquadro imgSkills" src="../assets/icons/html5.svg" alt="HTML5">
                    <img class="firstquadro imgSkills" src="../assets/icons/css3.svg" alt="css3">
                    <img class="firstquadro imgSkills" src="../assets/icons/javascript.svg" alt="javascript">
                    <img class="firstquadro imgSkills" src="../assets/icons/bootstrap.svg" alt="bootstrap">
                </div>
                <div class="quadrodois quadro">
                    <img class="secondquadro imgSkills" src="../assets/icons/vuejs.svg" alt="vuejs">
                    <img class="secondquadro imgSkills" src="../assets/icons/java.svg" alt="java">
                    <img class="secondquadro imgSkills" src="../assets/icons/git.svg" alt="git">
                    <img class="secondquadro imgSkills" src="../assets/icons/github.svg" alt="github">
                </div>
                <div class="quadrotres quadro">
                    <img class="treequadro imgSkills" src="../assets/icons/mongodb.svg" alt="mongodb">
                    <img class="treequadro imgSkills" src="../assets/icons/mysql.svg" alt="mysql">
                    <img class="treequadro imgSkills" src="../assets/icons/nodejs.svg" alt="nodejs">
                    <img class="treequadro imgSkills" src="../assets/icons/python.svg" alt="python">
                </div>
            </section>
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

    h1 {
        color: white;
        font-family: Arial, Helvetica, sans-serif;
    }
    
    #sobre {
        background-image: url("../assets/imagens/rodape-invertido2.png");
        background-repeat: no-repeat; 
    }

    .imgSkills {
        
        height: 50px;
        width: 50px;
    }

    section {
        display: grid;
        height: 300px;
        width: 300px;
        grid-auto-columns: 25% 25% 25% 25%;
        grid-auto-rows: 1fr 1fr 1fr;
        grid-template-areas: 
            "firstquadro"
            "secondquadro"
            "treequadro"
        ;

    }

    #skills {
        justify-content: space-around;
        align-items: center;
        margin: auto;
    }

    .quadro {
        display: flex;
        justify-content: space-around;
    }

    div {
        background: transparent;
    }

    .quadroum {
        grid-area: firstquadro;
        
    }

    .quadrodois {
        grid-area: secondquadro;

    }

    .quadrotres {
        grid-area: treequadro;
    }
    
</style>