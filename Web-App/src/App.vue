<template>
  <Header 
    :groupNames="groupNames" 
    @add-to-group-list="addToGroupList"
    @remove-from-group-list="removeFromGroupList"
    @change-seleckted-group="selectGroup"/>
  <GroupCard 
    v-for="gData in groupDatas" 
    v-bind:key="gData"
    :displayed="gData.name==selectedGroup"
    :groupData="gData"/>
</template>

<script>
  import Header from './components/Header.vue'
  import GroupCard from './components/GroupCard.vue'

  export default {
    name: 'App',
    components: {
      Header,
      GroupCard
    },
    data () {
      return {
        groupNames: [],
        groupDatas: [],
        selectedGroup: ""
      }
    },
    methods: {
      addToGroupList(gData) {
        console.log(4, gData, this.groupNames.indexOf(gData) == -1)
        if (this.groupNames.indexOf(gData) == -1) {
          console.log(5,gData.name)
          this.groupNames.push(gData.name)
          this.groupDatas.push(gData)
          this.selectedGroup = gData.name
        } 
      },

      selectGroup(gName) {
        this.selectedGroup = gName
      },
      removeFromGroupList(gName) {
        this.groupNames = this.groupNames.filter(el => el !== gName)
        this.groupData = this.groupData.filter( el => el.name === gName) 
      }
    }
  }
</script>

<style  lang="scss">

#app {
}

.search-input{

}



.fx-row{
  display: flex;
  flex-direction: row;
}

.fx-column{
  display: flex;
  flex-direction: column;
}

.fx-center {
  justify-content: center; 
}

.fx-flex-start{
  justify-content: flex-start; 
}

.fx-flex-end{
  justify-content: flex-end;
}

.fx-space-between{
  justify-content: space-between; 
}

.fx-space-evenly{
  justify-content: space-evenly; 
}

.fx-space-around{
  justify-content: space-around; 
}

.fx-align-start{
  align-self: self-start;
}

.fx-align-end{
  align-self: self-end;
}

.fx-align-center{
  align-self: center 
}

.hover-icon{
  transition: transform .2s;
  &:hover{
    transform: scale(1.25); 
    font-weight: 900
  }
}

</style>
