<template>
  <div class="container">
    <div class="row">
      <div v-if="this.questFinish == true">
        <h3 class="text-center">Resultado</h3>
            <div class="container my-5">
              <h4>Salário Hora : {{this.salario}}</h4>
              <h4>Horas Trabalhadas: {{this.horasTrab}}</h4>
              <h4>Salário Bruto: {{this.bruto}}</h4>
              <h4>INSS: {{this.inss}}</h4>
              <h4>Imposto de Renda: {{this.renda}}</h4>
              <h4>Salário Líquido: {{this.salarioLiquido}}</h4>
              <h4>Sindicato: {{this.sindicato}}</h4>
                <button type="button"
                  class="btn btn-primary
                  mt-5 mr-3 btn-lg"
                  v-on:click.stop.prevent = resetQuest
                  >Reiniciar</button>
            </div>
          </div>
      </div>
      <div v-if="this.questStart == true">
        <h1>Insira suas notas</h1>
        <hr>
      <div class="col-8">
         <b-form-group
            label="Insira seu salário hora e suas horas trabalhadas"
            label-for="input-formatter"
            class="mb-0"
          >
            <b-form-input
              type="number"
              id="addsalario"
              v-model="salario"
              placeholder="Salário Hora">
              </b-form-input>
            <br>
            <b-form-input
              type="number"
              id="addHoras"
              v-model="horasTrab"
              placeholder="Horas Trabalhadas"
            ></b-form-input>
          </b-form-group>
              <div class="float-right">
                  <button type="button"
                  class="btn btn-success
                  mt-5 mr-3 btn-lg"
                  v-on:click.stop.prevent = testes
                  >Calcular!</button>
              </div>
            </div>
       </div>
      </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      salario: '',
      horasTrab: '',
      inss: '',
      renda: '',
      sindicato: '',
      salarioLiquido: '',
      questFinish: false,
      questStart: true,
    };
  },
  methods: {
    postNumbers() {
      const path = 'http://localhost:5000/salario';
      this.salario = parseInt(this.salario, 10);
      this.horasTrab = parseInt(this.horasTrab, 10);
      const payload = {
        salario: this.salario,
        horasTrab: this.horasTrab,
      };
      axios.post(path, payload)
        .then((res) => {
          console.log(this.bruto);
          this.salario = res.data.salario;
          this.horasTrab = res.data.horasTrab;
          this.bruto = res.data.bruto;
          this.inss = res.data.inss;
          this.renda = res.data.renda;
          this.sindicato = res.data.sindicato;
          this.salarioLiquido = res.data.salarioLiquido;
          this.questFinished();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log('numdeu');
          console.log(error);
        });
      this.finished = true;
    },
    testes() {
      this.salario = parseInt(this.salario, 10);
      this.horasTrab = parseInt(this.horasTrab, 10);
      if (Number.isNaN(this.horasTrab) || Number.isNaN(this.salario)) {
        window.alert('Insira um valor!');
        this.horasTrab = null;
        this.salario = null;
      } else if (this.horasTrab <= 0 || this.salario <= 0) {
        window.alert('Insira um valor positivo!');
        this.horasTrab = null;
        this.salario = null;
      } else {
        this.postNumbers();
      }
    },
    questFinished() {
      this.questFinish = true;
      this.questStart = false;
    },
    resetQuest() {
      this.questFinish = false;
      this.questStart = true;
      this.reset();
    },
    reset() {
      this.finished = false;
      this.numbers = [];
      this.number = null;
    },
  },
};
</script>
