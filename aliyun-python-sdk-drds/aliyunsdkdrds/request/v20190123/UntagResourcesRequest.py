# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class UntagResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'UntagResources','drds')

	def get_All(self):
		return self.get_query_params().get('All')

	def set_All(self,All):
		self.add_query_param('All',All)

	def get_NoRole(self):
		return self.get_query_params().get('NoRole')

	def set_NoRole(self,NoRole):
		self.add_query_param('NoRole',NoRole)

	def get_ResourceIds(self):
		return self.get_query_params().get('ResourceIds')

	def set_ResourceIds(self,ResourceIds):
		for i in range(len(ResourceIds)):	
			if ResourceIds[i] is not None:
				self.add_query_param('ResourceId.' + str(i + 1) , ResourceIds[i]);

	def get_TagKeys(self):
		return self.get_query_params().get('TagKeys')

	def set_TagKeys(self,TagKeys):
		for i in range(len(TagKeys)):	
			if TagKeys[i] is not None:
				self.add_query_param('TagKey.' + str(i + 1) , TagKeys[i]);

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)