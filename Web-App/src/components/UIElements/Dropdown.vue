<template>
   <div  class="fx-column fx-space-between dropdown-wrapper" flex-direction=row>
        <div class="inner-wrapper" v-if="options.length > 0"> 
            <div v-for="option in options" :key="option" class="options" @click="select(option)">{{option}} </div>
        </div>  
   </div>

</template>

<script>


export default {
  name: 'Dropdown',
  props: {
    options: {
      required: true,
      type: Array
    }
  },
  components: {
  },
  data() {
    return {
      value: ""
    }
  },
  methods: {
    
    select(value) {
      this.$emit('select-option', value)
      return
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">  
.dropdown-wrapper{
    position: fixed;
    width: 100%;
    height: 0px;
    z-index: 100;
}
.inner-wrapper{
    background-color: white;
    border: 1px solid black;
    box-sizing: border-box; 
}

.options{
    position: relative;
    width: 100%;
    padding: .25em .25em .15em .5em;
    &:hover {
        background-color: #d1cac2;
    }
}

</style>
