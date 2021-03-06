# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ReservationList(ListResource):

    def __init__(self, version, workspace_sid, task_sid):
        """
        Initialize the ReservationList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_sid: The task_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        """
        super(ReservationList, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations'.format(**self._solution)

    def stream(self, reservation_status=values.unset, limit=None, page_size=None):
        """
        Streams ReservationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param ReservationInstance.Status reservation_status: The reservation_status
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            reservation_status=reservation_status,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, reservation_status=values.unset, limit=None, page_size=None):
        """
        Lists ReservationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param ReservationInstance.Status reservation_status: The reservation_status
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance]
        """
        return list(self.stream(
            reservation_status=reservation_status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, reservation_status=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ReservationInstance records from the API.
        Request is executed immediately

        :param ReservationInstance.Status reservation_status: The reservation_status
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        """
        params = values.of({
            'ReservationStatus': reservation_status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ReservationPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ReservationContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        return ReservationContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ReservationContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        return ReservationContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationList>'


class ReservationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ReservationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        :param task_sid: The task_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        """
        super(ReservationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ReservationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        return ReservationInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationPage>'


class ReservationContext(InstanceContext):

    def __init__(self, version, workspace_sid, task_sid, sid):
        """
        Initialize the ReservationContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_sid: The task_sid
        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        super(ReservationContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ReservationInstance

        :returns: Fetched ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ReservationInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=self._solution['sid'],
        )

    def update(self, reservation_status=values.unset,
               worker_activity_sid=values.unset, instruction=values.unset,
               dequeue_post_work_activity_sid=values.unset,
               dequeue_from=values.unset, dequeue_record=values.unset,
               dequeue_timeout=values.unset, dequeue_to=values.unset,
               dequeue_status_callback_url=values.unset, call_from=values.unset,
               call_record=values.unset, call_timeout=values.unset,
               call_to=values.unset, call_url=values.unset,
               call_status_callback_url=values.unset, call_accept=values.unset,
               redirect_call_sid=values.unset, redirect_accept=values.unset,
               redirect_url=values.unset):
        """
        Update the ReservationInstance

        :param ReservationInstance.Status reservation_status: The reservation_status
        :param unicode worker_activity_sid: The worker_activity_sid
        :param unicode instruction: The instruction
        :param unicode dequeue_post_work_activity_sid: The dequeue_post_work_activity_sid
        :param unicode dequeue_from: The dequeue_from
        :param unicode dequeue_record: The dequeue_record
        :param unicode dequeue_timeout: The dequeue_timeout
        :param unicode dequeue_to: The dequeue_to
        :param unicode dequeue_status_callback_url: The dequeue_status_callback_url
        :param unicode call_from: The call_from
        :param unicode call_record: The call_record
        :param unicode call_timeout: The call_timeout
        :param unicode call_to: The call_to
        :param unicode call_url: The call_url
        :param unicode call_status_callback_url: The call_status_callback_url
        :param bool call_accept: The call_accept
        :param unicode redirect_call_sid: The redirect_call_sid
        :param bool redirect_accept: The redirect_accept
        :param unicode redirect_url: The redirect_url

        :returns: Updated ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        data = values.of({
            'ReservationStatus': reservation_status,
            'WorkerActivitySid': worker_activity_sid,
            'Instruction': instruction,
            'DequeuePostWorkActivitySid': dequeue_post_work_activity_sid,
            'DequeueFrom': dequeue_from,
            'DequeueRecord': dequeue_record,
            'DequeueTimeout': dequeue_timeout,
            'DequeueTo': dequeue_to,
            'DequeueStatusCallbackUrl': dequeue_status_callback_url,
            'CallFrom': call_from,
            'CallRecord': call_record,
            'CallTimeout': call_timeout,
            'CallTo': call_to,
            'CallUrl': call_url,
            'CallStatusCallbackUrl': call_status_callback_url,
            'CallAccept': call_accept,
            'RedirectCallSid': redirect_call_sid,
            'RedirectAccept': redirect_accept,
            'RedirectUrl': redirect_url,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ReservationInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ReservationContext {}>'.format(context)


class ReservationInstance(InstanceResource):

    class Status(object):
        PENDING = "pending"
        ACCEPTED = "accepted"
        REJECTED = "rejected"
        TIMEOUT = "timeout"
        CANCELED = "canceled"
        RESCINDED = "rescinded"

    def __init__(self, version, payload, workspace_sid, task_sid, sid=None):
        """
        Initialize the ReservationInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        super(ReservationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'reservation_status': payload['reservation_status'],
            'sid': payload['sid'],
            'task_sid': payload['task_sid'],
            'worker_name': payload['worker_name'],
            'worker_sid': payload['worker_sid'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ReservationContext for this ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        if self._context is None:
            self._context = ReservationContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_sid=self._solution['task_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def reservation_status(self):
        """
        :returns: The reservation_status
        :rtype: ReservationInstance.Status
        """
        return self._properties['reservation_status']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def task_sid(self):
        """
        :returns: The task_sid
        :rtype: unicode
        """
        return self._properties['task_sid']

    @property
    def worker_name(self):
        """
        :returns: The worker_name
        :rtype: unicode
        """
        return self._properties['worker_name']

    @property
    def worker_sid(self):
        """
        :returns: The worker_sid
        :rtype: unicode
        """
        return self._properties['worker_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a ReservationInstance

        :returns: Fetched ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        return self._proxy.fetch()

    def update(self, reservation_status=values.unset,
               worker_activity_sid=values.unset, instruction=values.unset,
               dequeue_post_work_activity_sid=values.unset,
               dequeue_from=values.unset, dequeue_record=values.unset,
               dequeue_timeout=values.unset, dequeue_to=values.unset,
               dequeue_status_callback_url=values.unset, call_from=values.unset,
               call_record=values.unset, call_timeout=values.unset,
               call_to=values.unset, call_url=values.unset,
               call_status_callback_url=values.unset, call_accept=values.unset,
               redirect_call_sid=values.unset, redirect_accept=values.unset,
               redirect_url=values.unset):
        """
        Update the ReservationInstance

        :param ReservationInstance.Status reservation_status: The reservation_status
        :param unicode worker_activity_sid: The worker_activity_sid
        :param unicode instruction: The instruction
        :param unicode dequeue_post_work_activity_sid: The dequeue_post_work_activity_sid
        :param unicode dequeue_from: The dequeue_from
        :param unicode dequeue_record: The dequeue_record
        :param unicode dequeue_timeout: The dequeue_timeout
        :param unicode dequeue_to: The dequeue_to
        :param unicode dequeue_status_callback_url: The dequeue_status_callback_url
        :param unicode call_from: The call_from
        :param unicode call_record: The call_record
        :param unicode call_timeout: The call_timeout
        :param unicode call_to: The call_to
        :param unicode call_url: The call_url
        :param unicode call_status_callback_url: The call_status_callback_url
        :param bool call_accept: The call_accept
        :param unicode redirect_call_sid: The redirect_call_sid
        :param bool redirect_accept: The redirect_accept
        :param unicode redirect_url: The redirect_url

        :returns: Updated ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        return self._proxy.update(
            reservation_status=reservation_status,
            worker_activity_sid=worker_activity_sid,
            instruction=instruction,
            dequeue_post_work_activity_sid=dequeue_post_work_activity_sid,
            dequeue_from=dequeue_from,
            dequeue_record=dequeue_record,
            dequeue_timeout=dequeue_timeout,
            dequeue_to=dequeue_to,
            dequeue_status_callback_url=dequeue_status_callback_url,
            call_from=call_from,
            call_record=call_record,
            call_timeout=call_timeout,
            call_to=call_to,
            call_url=call_url,
            call_status_callback_url=call_status_callback_url,
            call_accept=call_accept,
            redirect_call_sid=redirect_call_sid,
            redirect_accept=redirect_accept,
            redirect_url=redirect_url,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ReservationInstance {}>'.format(context)
