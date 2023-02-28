# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List
import time
import random
import logging
from ..errors import OperationTimeout, OperationFailed

_LOG = logging.getLogger('databricks.sdk.service.endpoints')

# all definitions in this file are in alphabetical order


@dataclass
class BuildLogsRequest:
    """Retrieve the logs associated with building the model's environment for a given serving
    endpoint's served model."""

    name: str
    served_model_name: str


@dataclass
class BuildLogsResponse:
    logs: str

    def as_dict(self) -> dict:
        body = {}
        if self.logs: body['logs'] = self.logs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'BuildLogsResponse':
        return cls(logs=d.get('logs', None))


@dataclass
class CreateServingEndpoint:
    config: 'EndpointCoreConfigInput'
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'CreateServingEndpoint':
        return cls(config=EndpointCoreConfigInput.from_dict(d['config']) if 'config' in d else None,
                   name=d.get('name', None))


@dataclass
class DeleteServingEndpointRequest:
    """Delete a serving endpoint"""

    name: str


@dataclass
class EndpointCoreConfigInput:
    name: str
    served_models: 'List[ServedModelInput]'
    traffic_config: 'TrafficConfig'

    def as_dict(self) -> dict:
        body = {}
        if self.name: body['name'] = self.name
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointCoreConfigInput':
        return cls(
            name=d.get('name', None),
            served_models=[ServedModelInput.from_dict(v) for v in d['served_models']]
            if 'served_models' in d and d['served_models'] is not None else None,
            traffic_config=TrafficConfig.from_dict(d['traffic_config']) if 'traffic_config' in d else None)


@dataclass
class EndpointCoreConfigOutput:
    config_version: int
    served_models: 'List[ServedModelOutput]'
    traffic_config: 'TrafficConfig'

    def as_dict(self) -> dict:
        body = {}
        if self.config_version: body['config_version'] = self.config_version
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointCoreConfigOutput':
        return cls(
            config_version=d.get('config_version', None),
            served_models=[ServedModelOutput.from_dict(v) for v in d['served_models']]
            if 'served_models' in d and d['served_models'] is not None else None,
            traffic_config=TrafficConfig.from_dict(d['traffic_config']) if 'traffic_config' in d else None)


@dataclass
class EndpointCoreConfigSummary:
    served_models: 'List[ServedModelSpec]'

    def as_dict(self) -> dict:
        body = {}
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointCoreConfigSummary':
        return cls(served_models=[ServedModelSpec.from_dict(v) for v in d['served_models']]
                   if 'served_models' in d and d['served_models'] is not None else None)


@dataclass
class EndpointPendingConfig:
    config_version: int
    served_models: 'List[ServedModelOutput]'
    start_time: int
    traffic_config: 'TrafficConfig'

    def as_dict(self) -> dict:
        body = {}
        if self.config_version: body['config_version'] = self.config_version
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.start_time: body['start_time'] = self.start_time
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointPendingConfig':
        return cls(
            config_version=d.get('config_version', None),
            served_models=[ServedModelOutput.from_dict(v) for v in d['served_models']]
            if 'served_models' in d and d['served_models'] is not None else None,
            start_time=d.get('start_time', None),
            traffic_config=TrafficConfig.from_dict(d['traffic_config']) if 'traffic_config' in d else None)


@dataclass
class EndpointState:
    config_update: 'EndpointStateConfigUpdate'
    ready: 'EndpointStateReady'

    def as_dict(self) -> dict:
        body = {}
        if self.config_update: body['config_update'] = self.config_update.value
        if self.ready: body['ready'] = self.ready.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'EndpointState':
        return cls(
            config_update=EndpointStateConfigUpdate(d['config_update']) if 'config_update' in d else None,
            ready=EndpointStateReady(d['ready']) if 'ready' in d else None)


class EndpointStateConfigUpdate(Enum):
    """The state of an endpoint's config update. This informs the user if the pending_config is in
    progress, if the update failed, or if there is no update in progress. Note that if the
    endpoint's config_update state value is IN_PROGRESS, another update can not be made until the
    update completes or fails."""

    IN_PROGRESS = 'IN_PROGRESS'
    NOT_UPDATING = 'NOT_UPDATING'
    UPDATE_FAILED = 'UPDATE_FAILED'


class EndpointStateReady(Enum):
    """The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is
    READY if all of the served models in its active configuration are ready. If any of the actively
    served models are in a non-ready state, the endpoint state will be NOT_READY."""

    NOT_READY = 'NOT_READY'
    READY = 'READY'


@dataclass
class ExportMetricsRequest:
    """Retrieve the metrics corresponding to a serving endpoint for the current time in Prometheus or
    OpenMetrics exposition format"""

    name: str


@dataclass
class GetServingEndpointRequest:
    """Get a single serving endpoint"""

    name: str


@dataclass
class ListEndpointsResponse:
    endpoints: 'List[ServingEndpoint]'

    def as_dict(self) -> dict:
        body = {}
        if self.endpoints: body['endpoints'] = [v.as_dict() for v in self.endpoints]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListEndpointsResponse':
        return cls(
            endpoints=[ServingEndpoint.from_dict(v)
                       for v in d['endpoints']] if 'endpoints' in d and d['endpoints'] is not None else None)


@dataclass
class LogsRequest:
    """Retrieve the most recent log lines associated with a given serving endpoint's served model"""

    name: str
    served_model_name: str


@dataclass
class QueryEndpointResponse:
    predictions: 'List[Any]'

    def as_dict(self) -> dict:
        body = {}
        if self.predictions: body['predictions'] = [v for v in self.predictions]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'QueryEndpointResponse':
        return cls(predictions=d.get('predictions', None))


@dataclass
class QueryRequest:
    """Query a serving endpoint with provided model input."""

    name: str


@dataclass
class Route:
    served_model_name: str
    traffic_percentage: int

    def as_dict(self) -> dict:
        body = {}
        if self.served_model_name: body['served_model_name'] = self.served_model_name
        if self.traffic_percentage: body['traffic_percentage'] = self.traffic_percentage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Route':
        return cls(served_model_name=d.get('served_model_name', None),
                   traffic_percentage=d.get('traffic_percentage', None))


@dataclass
class ServedModelInput:
    model_name: str
    model_version: str
    name: str
    scale_to_zero_enabled: bool
    workload_size: str

    def as_dict(self) -> dict:
        body = {}
        if self.model_name: body['model_name'] = self.model_name
        if self.model_version: body['model_version'] = self.model_version
        if self.name: body['name'] = self.name
        if self.scale_to_zero_enabled: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.workload_size: body['workload_size'] = self.workload_size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelInput':
        return cls(model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   workload_size=d.get('workload_size', None))


@dataclass
class ServedModelOutput:
    creation_timestamp: int
    creator: str
    model_name: str
    model_version: str
    name: str
    scale_to_zero_enabled: bool
    state: 'ServedModelState'

    def as_dict(self) -> dict:
        body = {}
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.creator: body['creator'] = self.creator
        if self.model_name: body['model_name'] = self.model_name
        if self.model_version: body['model_version'] = self.model_version
        if self.name: body['name'] = self.name
        if self.scale_to_zero_enabled: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.state: body['state'] = self.state.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelOutput':
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   state=ServedModelState.from_dict(d['state']) if 'state' in d else None)


@dataclass
class ServedModelSpec:
    model_name: str
    model_version: str
    name: str

    def as_dict(self) -> dict:
        body = {}
        if self.model_name: body['model_name'] = self.model_name
        if self.model_version: body['model_version'] = self.model_version
        if self.name: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelSpec':
        return cls(model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None))


@dataclass
class ServedModelState:
    deployment: 'ServedModelStateDeployment'
    deployment_state_message: str

    def as_dict(self) -> dict:
        body = {}
        if self.deployment: body['deployment'] = self.deployment.value
        if self.deployment_state_message: body['deployment_state_message'] = self.deployment_state_message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServedModelState':
        return cls(deployment=ServedModelStateDeployment(d['deployment']) if 'deployment' in d else None,
                   deployment_state_message=d.get('deployment_state_message', None))


class ServedModelStateDeployment(Enum):
    """The state of the served model deployment. DEPLOYMENT_CREATING indicates that the served model is
    not ready yet because the deployment is still being created (i.e container image is building,
    model server is deploying for the first time, etc.). DEPLOYMENT_RECOVERING indicates that the
    served model was previously in a ready state but no longer is and is attempting to recover.
    DEPLOYMENT_READY indicates that the served model is ready to receive traffic. DEPLOYMENT_FAILED
    indicates that there was an error trying to bring up the served model (e.g container image build
    failed, the model server failed to start due to a model loading error, etc.) DEPLOYMENT_ABORTED
    indicates that the deployment was terminated likely due to a failure in bringing up another
    served model under the same endpoint and config version."""

    DEPLOYMENT_ABORTED = 'DEPLOYMENT_ABORTED'
    DEPLOYMENT_CREATING = 'DEPLOYMENT_CREATING'
    DEPLOYMENT_FAILED = 'DEPLOYMENT_FAILED'
    DEPLOYMENT_READY = 'DEPLOYMENT_READY'
    DEPLOYMENT_RECOVERING = 'DEPLOYMENT_RECOVERING'


@dataclass
class ServerLogsResponse:
    logs: str

    def as_dict(self) -> dict:
        body = {}
        if self.logs: body['logs'] = self.logs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServerLogsResponse':
        return cls(logs=d.get('logs', None))


@dataclass
class ServingEndpoint:
    config: 'EndpointCoreConfigSummary'
    creation_timestamp: int
    creator: str
    id: str
    last_updated_timestamp: int
    name: str
    state: 'EndpointState'

    def as_dict(self) -> dict:
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.creator: body['creator'] = self.creator
        if self.id: body['id'] = self.id
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name: body['name'] = self.name
        if self.state: body['state'] = self.state.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServingEndpoint':
        return cls(config=EndpointCoreConfigSummary.from_dict(d['config']) if 'config' in d else None,
                   creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   state=EndpointState.from_dict(d['state']) if 'state' in d else None)


@dataclass
class ServingEndpointDetailed:
    config: 'EndpointCoreConfigOutput'
    creation_timestamp: int
    creator: str
    id: str
    last_updated_timestamp: int
    name: str
    pending_config: 'EndpointPendingConfig'
    permission_level: 'ServingEndpointDetailedPermissionLevel'
    state: 'EndpointState'

    def as_dict(self) -> dict:
        body = {}
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_timestamp: body['creation_timestamp'] = self.creation_timestamp
        if self.creator: body['creator'] = self.creator
        if self.id: body['id'] = self.id
        if self.last_updated_timestamp: body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name: body['name'] = self.name
        if self.pending_config: body['pending_config'] = self.pending_config.as_dict()
        if self.permission_level: body['permission_level'] = self.permission_level.value
        if self.state: body['state'] = self.state.as_dict()
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ServingEndpointDetailed':
        return cls(config=EndpointCoreConfigOutput.from_dict(d['config']) if 'config' in d else None,
                   creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   pending_config=EndpointPendingConfig.from_dict(d['pending_config'])
                   if 'pending_config' in d else None,
                   permission_level=ServingEndpointDetailedPermissionLevel(d['permission_level'])
                   if 'permission_level' in d else None,
                   state=EndpointState.from_dict(d['state']) if 'state' in d else None)


class ServingEndpointDetailedPermissionLevel(Enum):
    """The permission level of the principal making the request."""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_QUERY = 'CAN_QUERY'
    CAN_VIEW = 'CAN_VIEW'


@dataclass
class TrafficConfig:
    routes: 'List[Route]'

    def as_dict(self) -> dict:
        body = {}
        if self.routes: body['routes'] = [v.as_dict() for v in self.routes]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'TrafficConfig':
        return cls(routes=[Route.from_dict(v)
                           for v in d['routes']] if 'routes' in d and d['routes'] is not None else None)


class ServingEndpointsAPI:
    """The Serverless Real-Time Inference Serving Endpoints API allows you to create, update, and delete model
    serving endpoints.
    
    You can use a serving endpoint to serve models from the Databricks Model Registry. Endpoints expose the
    underlying models as scalable REST API endpoints using serverless compute. This means the endpoints and
    associated compute resources are fully managed by Databricks and will not appear in your cloud account. A
    serving endpoint can consist of one or more MLflow models from the Databricks Model Registry, called
    served models. A serving endpoint can have at most ten served models. You can configure traffic settings
    to define how requests should be routed to your served models behind an endpoint. Additionally, you can
    configure the scale of resources that should be applied to each served model."""

    def __init__(self, api_client):
        self._api = api_client

    def build_logs(self, name: str, served_model_name: str, **kwargs) -> BuildLogsResponse:
        """Retrieve the logs associated with building the model's environment for a given serving endpoint's
        served model.
        
        Retrieves the build logs associated with the provided served model. Please note that this API is in
        preview and may change in the future."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = BuildLogsRequest(name=name, served_model_name=served_model_name)

        json = self._api.do(
            'GET',
            f'/api/2.0/serving-endpoints/{request.name}/served-models/{request.served_model_name}/build-logs')
        return BuildLogsResponse.from_dict(json)

    def create(self,
               name: str,
               config: EndpointCoreConfigInput,
               wait=True,
               timeout=20,
               **kwargs) -> ServingEndpointDetailed:
        """Create a new serving endpoint."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = CreateServingEndpoint(config=config, name=name)
        body = request.as_dict()
        if wait:
            op_response = self._api.do('POST', '/api/2.0/serving-endpoints', body=body)
            started = time.time()
            target_states = (EndpointStateConfigUpdate.NOT_UPDATING, )
            failure_states = (EndpointStateConfigUpdate.UPDATE_FAILED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(name=op_response['name'])
                status = poll.state.config_update
                status_message = f'current status: {status}'
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach NOT_UPDATING, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"serving_endpoints.get(name={op_response['name']})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('POST', '/api/2.0/serving-endpoints', body=body)

    def delete(self, name: str, **kwargs):
        """Delete a serving endpoint."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = DeleteServingEndpointRequest(name=name)

        self._api.do('DELETE', f'/api/2.0/serving-endpoints/{request.name}')

    def export_metrics(self, name: str, **kwargs):
        """Retrieve the metrics corresponding to a serving endpoint for the current time in Prometheus or
        OpenMetrics exposition format.
        
        Retrieves the metrics associated with the provided serving endpoint in either Prometheus or
        OpenMetrics exposition format. Please note that this API is in preview and may change in the future."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ExportMetricsRequest(name=name)

        self._api.do('GET', f'/api/2.0/serving-endpoints/{request.name}/metrics')

    def get(self, name: str, **kwargs) -> ServingEndpointDetailed:
        """Get a single serving endpoint.
        
        Retrieves the details for a single serving endpoint."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetServingEndpointRequest(name=name)

        json = self._api.do('GET', f'/api/2.0/serving-endpoints/{request.name}')
        return ServingEndpointDetailed.from_dict(json)

    def list(self) -> ListEndpointsResponse:
        """Retrieve all serving endpoints."""

        json = self._api.do('GET', '/api/2.0/serving-endpoints')
        return ListEndpointsResponse.from_dict(json)

    def logs(self, name: str, served_model_name: str, **kwargs) -> ServerLogsResponse:
        """Retrieve the most recent log lines associated with a given serving endpoint's served model.
        
        Retrieves the service logs associated with the provided served model. Please note that this API is in
        preview and may change in the future."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = LogsRequest(name=name, served_model_name=served_model_name)

        json = self._api.do(
            'GET',
            f'/api/2.0/serving-endpoints/{request.name}/served-models/{request.served_model_name}/logs')
        return ServerLogsResponse.from_dict(json)

    def query(self, name: str, **kwargs) -> QueryEndpointResponse:
        """Query a serving endpoint with provided model input."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = QueryRequest(name=name)

        json = self._api.do('POST', f'/serving-endpoints/{request.name}/invocations')
        return QueryEndpointResponse.from_dict(json)

    def update_config(self,
                      served_models: List[ServedModelInput],
                      name: str,
                      *,
                      traffic_config: TrafficConfig = None,
                      wait=True,
                      timeout=20,
                      **kwargs) -> ServingEndpointDetailed:
        """Update a serving endpoint with a new config.
        
        Updates any combination of the serving endpoint's served models, the compute configuration of those
        served models, and the endpoint's traffic config. An endpoint that already has an update in progress
        can not be updated until the current update completes or fails."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = EndpointCoreConfigInput(name=name,
                                              served_models=served_models,
                                              traffic_config=traffic_config)
        body = request.as_dict()
        if wait:
            op_response = self._api.do('PUT', f'/api/2.0/serving-endpoints/{request.name}/config', body=body)
            started = time.time()
            target_states = (EndpointStateConfigUpdate.NOT_UPDATING, )
            failure_states = (EndpointStateConfigUpdate.UPDATE_FAILED, )
            status_message = 'polling...'
            attempt = 1
            while (started + (timeout * 60)) > time.time():
                poll = self.get(name=op_response['name'])
                status = poll.state.config_update
                status_message = f'current status: {status}'
                if status in target_states:
                    return poll
                if status in failure_states:
                    msg = f'failed to reach NOT_UPDATING, got {status}: {status_message}'
                    raise OperationFailed(msg)
                prefix = f"serving_endpoints.get(name={op_response['name']})"
                sleep = attempt
                if sleep > 10:
                    # sleep 10s max per attempt
                    sleep = 10
                _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
                time.sleep(sleep + random.random())
                attempt += 1
            raise OperationTimeout(f'timed out after {timeout} minutes: {status_message}')
        self._api.do('PUT', f'/api/2.0/serving-endpoints/{request.name}/config', body=body)
