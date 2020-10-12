<template>
  <div  class="fx-row fx-space-between header">
      <div class="content">{{ title }}</div>
      <div class="fx-row content fx-align-center">
      <div v-for="gName in groupNames" :key="gName" >
        <div class="fx-row fx-space-between stock-tap" @click="changeSelecktedGroup(gName)">
          <p class="stock-title" >{{gName}}</p>
          <span class="fx-align-end fx-flex-end hover-icon" @click="removeFromGroupList($event, gName)"> <Close theme="filled"/></span>
        </div>
      </div>
      <div class="fx-column">
        <form class="review-form" @submit.prevent="onSubmit">
          <input id="name" class="search-input" v-model="groupName">
         <!-- <Dropdown :options="tickerSugestions" @select-option="onSubmit"></Dropdown> -->
        </form>
      </div>
    </div>
 </div>

</template>

<script>

import GithubService from '../services/githubService.js';
// import Dropdown from './UIElements/Dropdown.vue';
import {Close} from '@icon-park/vue-next';

export default {
  name: 'Header',
  props: {
    groupNames: {
    },
    selectedGroupName: {
      required: false
    }
  },
  components: {
    // Dropdown,
    Close
  },
  data() {
    return {
      title: "Git Pullrequest Overview",
      groupName:"PyGithub",
      groupData: ''
    }
  },
  methods: {
    
    removeFromStockList(event, gName) {
      event.stopPropagation() 
      this.$emit('remove-from-grpup-list', gName)
      
    },
    changeSelecktedGroup(gName) {
      this.$emit('change-seleckted-group', gName)
    },

    async onSubmit() {
      if (!event.altKey && !event.ctrlKey) {
        var gs = new GithubService()
        var groupData = await gs.getGroupRepos(this.groupName)
        if (groupData !== false) {
          this.groupData = groupData.data
          this.$emit('add-to-group-list', {name: this.groupName, data: this.groupData})
          this.groupName = ""
        } else {
          console.log('name do not exist')
        }
        return 
      }




      // if(value) name = value
      // this.groupNameName = ""
      return
    }
  }


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">  
  .content {
    width: auto;
    margin: 0.25em;
  }

  .header{
    border: 2px solid black;
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    font-size: 1.15em;
    font-weight: 600;  
    width: 100%
  }

  .stock-title{
    margin: auto 1em auto 0;
    font-size: 1.25em;
    font-weight: 600;
  }
  .stock-tap{
    border: 1px solid gray;
    border-radius: 0.5em;
    width: auto;
    font-size: 0.7em;
    padding: 0.15em .25em 0 .25em;
    margin-right: 0.5em;
    background-color: #c5d3de;
    &:hover{ 
      background-color: #ded2c5;
    }
  }

</style>
