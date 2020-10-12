<template>
  <div class="stock-card"> 
    <div class="stock-header">{{groupData.name}}</div>
    <div class="fx-column fx-flex-start">
      <div
        v-for="repoData in groupData.data" 
        v-bind:key="repoData">
          <div class="stock-sub-header">{{repoData.name}}</div>
        <div 
          v-for="prData in repoData.pullrequests" 
          v-bind:key="prData"
          class="pullrequest fx-row fx-flex-start"
          > 
            <span class="space"> {{prData.state}}</span>
            <span> {{prData.title }}</span>
            <span v-if="prData.user"> created by</span>
            <span> {{prData.user}}</span>
        </div>
      </div> 
    </div>
  </div>
</template>

<script>
  // import GithubService from '../services/githubService.js';

  export default {
    name: 'GroupCard',
    props: {
      groupData:{
        required: true,
      },
      displayed: {
        required: true,
      }
    },
    data() {
      return {
        isLoaded: false
      }
    },
    created() {
      console.log(this.groupData)
    },
    methods: {
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.stock-card{
  padding-top: 1em;
  padding-bottom: 1em;
}

.stock-header{
  background-color: gray;
  color: white;
  font-weight: 700;
  font-size: 1.3em;
  padding: 0.25em 0.25em 0.25em 0.5em;
}
.stock-sub-header{
  font-weight: 600;
  font-size: 1em;
  padding: 0.25em 0.25em 0.25em 0.5em;
}
.pullrequest{
  margin-left:3em;
  }
span{
  margin-right: 0.5em;  
}
</style>
