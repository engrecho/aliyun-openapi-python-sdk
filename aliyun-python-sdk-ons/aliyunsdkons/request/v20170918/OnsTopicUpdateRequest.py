# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class OnsTopicUpdateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ons', '2017-09-18', 'OnsTopicUpdate')

	def get_PreventCache(self):
		return self.get_query_params().get('PreventCache')

	def set_PreventCache(self,PreventCache):
		self.add_query_param('PreventCache',PreventCache)

	def get_OnsRegionId(self):
		return self.get_query_params().get('OnsRegionId')

	def set_OnsRegionId(self,OnsRegionId):
		self.add_query_param('OnsRegionId',OnsRegionId)

	def get_OnsPlatform(self):
		return self.get_query_params().get('OnsPlatform')

	def set_OnsPlatform(self,OnsPlatform):
		self.add_query_param('OnsPlatform',OnsPlatform)

	def get_Perm(self):
		return self.get_query_params().get('Perm')

	def set_Perm(self,Perm):
		self.add_query_param('Perm',Perm)

	def get_Topic(self):
		return self.get_query_params().get('Topic')

	def set_Topic(self,Topic):
		self.add_query_param('Topic',Topic)